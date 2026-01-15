from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from employees.models import Employee, Item
from .serializers import StudentSerializer, EmployeeSerializer, ItemSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics


# Create your views here.
@api_view(['GET','POST'])
def student(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED) 
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])    
def getDetails(request,pk):
    try:
        details = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(details)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StudentSerializer(details,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#   so whatever we've done till here is functon based views
#   where we use conditionals to select the request method
#   NOW, we'll use class-based views

class Employees(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    def get_object(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        details = self.get_object(pk)
        serializer = EmployeeSerializer(details)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        details = self.get_object(pk)
        serializer = EmployeeSerializer(details, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        detail = self.get_object(pk)
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#  Here we will be using Mixin and Generics to write the apis
class Items(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self,request):
        return self.list(request)
    
    def put(self,request):
        return self.create(request)