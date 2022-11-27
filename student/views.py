from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes
import json

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class=StudentSerializer

class apiView

# @api_view(['POST'])
# def studentLogin(request):
#     request_data = json.load(request)
#     email=request_data.get('email')
#     password=request_data.get('password')
#     user = Student.objects.filter(Email=email,Password=password,isActive=True)
#     content = StudentSerializer(user, many=True).data
#     if content!=[]:
#          return Response({"Email":email,"Password":password},status=200)
#     else:
#         return Response({"message":"Invald credentials"},status=400)



# @api_view(['Post'])
# def getLoggedinstudent(request):
#     request_data = json.load(request)
#     email=request_data.get('Email')
#     password=request_data.get('Password')
#     user = Student.objects.filter(Email=email,Password=password,isActive=True)
#     content = StudentSerializer(user, many=True).data
#     if content!=[]:
#          return Response({"data":content},status=200)
#     else:
#         return Response({"message":"Invald request"},status=400)