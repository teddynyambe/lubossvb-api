from django.shortcuts import get_object_or_404, render
from django.db.models import F
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from member_app.models import Member
from .models import Declaration
from .serializers import DeclareSerializer


@api_view(['POST'])
def save_declaration(request):
    if request.method == 'POST':

        serializer = DeclareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get member declaration


@api_view(['GET'])
def get_all_declarations(request):
    if request.method == 'GET':
        # Extract member_id from the request headers
        member_id = request.headers.get('member', None)

        if member_id is None:
            # If member_id is not provided, return 404
            return Response({"error": "member_id header is missing"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the member exists and return 404 if not
        get_object_or_404(Member, member_id=member_id)

        # Assuming the member exists, filter declarations by member_id
        declarations = Declaration.objects.filter(member_id=member_id)

        serializer = DeclareSerializer(declarations, many=True)
        return Response(serializer.data)

# Get all declarations


@api_view(['GET'])
def get_all_declarations_made(request):
    if request.method == 'GET':

        # Assuming the member exists, filter declarations by member_id
        declarations = Declaration.objects.all()

        serializer = DeclareSerializer(declarations, many=True)
        return Response(serializer.data)
