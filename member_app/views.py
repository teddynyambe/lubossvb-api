from django.shortcuts import render

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


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    # Extract user data from request
    # username = request.data.get('username')
    # password = request.data.get('password')
    # role = request.data.get('role')

    # first_name = request.data.get('first_name', '')
    # last_name = request.data.get('last_name', '')
    # nrc = request.data.get('nrc')

    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user = user_serializer.save()
        role = request.data.get('role')

        # Assign user to group based on role
        if role == 'Admin':
            group, _ = Group.objects.get_or_create(name='Admin')
        else:
            group, _ = Group.objects.get_or_create(name='Member')
        user.groups.add(group)

        # Now handle Member creation or updating
        member_data = request.data.copy()
        # Add the user instance to the member data
        member_data['user'] = user.pk
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
        return Response({'token': token.key}, status=status.HTTP_200_OK)
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
