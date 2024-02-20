from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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


@api_view(['GET'])
def get_all_declarations(request):
    if request.method == 'GET':
        declarations = Declaration.objects.all()
        serializer = DeclareSerializer(declarations, many=True)
        return Response(serializer.data)
