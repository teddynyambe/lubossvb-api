import uuid
from django.shortcuts import get_object_or_404, render

# account_app/views.py
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Member
from .serializers import MemberSerializer, UserSerializer
from django.contrib.auth.hashers import make_password


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# def register_user(request):
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        # Modify validated_data directly before saving
        user_serializer.validated_data['is_active'] = False
        user = user_serializer.save()
        user.is_active = False
        user.save()

        role = request.data.get('role')

        # Assign user to group based on role
        if role == 'Admin':
            group, _ = Group.objects.get_or_create(name='Admin')
        else:
            group, _ = Group.objects.get_or_create(name='Member')
        user.groups.add(group)

        # Now handle Member creation or updating
        member_data = request.data.copy()
        member_data.pop('member_id', None)

        # Add the user instance to the member data
        member_data['user_id'] = user.pk
        member_serializer = MemberSerializer(data=member_data)

        if member_serializer.is_valid():
            member_serializer.save()
            return Response({'status': True}, status=status.HTTP_201_CREATED)
        else:
            user.delete()  # Cleanup if member creation fails
            return Response(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Authenticate the user
    user = authenticate(username=username, password=password)
    if user:
        # If authentication is successful, get or create a token
        token, created = Token.objects.get_or_create(user=user)

        # Grab the role
        # Fetch user's groups (roles)
        groups = user.groups.all()
        roles = [group.name for group in groups]

        # Grab member related data
        member = Member.objects.get(user=user)

        member_data = {
            'first_name': member.first_name,
            'last_name': member.last_name,
            'member_id': member.member_id
        }

        return Response({
            'token': token.key,
            'username': user.username,
            'role': roles,
            'member': member_data}, status=status.HTTP_200_OK)
    else:
        # If authentication fails, return an error
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def member_list(request):
    """
    List all members.
    """
    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

# Approve Member joining group


# @api_view('POST')
# @permission_classes([IsAdminUser])
# def approve_member(request):
#     """
#     Approve member by admin
#     """

@api_view(['PUT'])
def user_member_update(request, pk):
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return Response({'error': 'Member not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = MemberSerializer(
        member, data=request.data, partial=True)  # Allow partial updates
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# def user_member_update(request):
    # if request.method == 'PUT':

    #     username = request.data.get('username')

    #     print(f"Username: {username}")

    #     user = get_object_or_404(User, username=username)

    #     if request.data.get('password') == 'no_change':
    #         pass
    #     else:
    #         new_password = make_password(request.data.get('password'))
    #         user.password = new_password

    #     member = get_object_or_404(Member, user=user)

    #     user_serializer = UserSerializer(user, data=request.data)
    #     if not user_serializer.is_valid():
    #         return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     member_serializer = MemberSerializer(member, data=request.data)
    #     if not member_serializer.is_valid():
    #         return Response(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     user_serializer.save()
    #     member_serializer.save()
    #     return Response(member_serializer.data, status=status.HTTP_200_OK)
