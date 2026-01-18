from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from employees.models import Employee, Item, User, Book, Designation
from .serializers import StudentSerializer, EmployeeSerializer, ItemSerializer, UserSerializer, BookSerializer, DesignationSerializer
from rest_framework.decorators import api_view      #for function based views
from rest_framework import status
from rest_framework.views import APIView            #for class based views
from django.http import Http404
from rest_framework import mixins, generics         #for class based views using mixin and generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404      #to aceess models in viewset
from blog.models import Blog,Comment
from blog.serializers import BlogSerializer,CommentSerializer

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

#  Here we will be using Mixins and Generics to write the apis
class Items(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self,request):
        return self.list(request)
    
    def put(self,request):
        return self.create(request)

class ItemDetails(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self,request,pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)


#now we'll see more advanced and convenient way using genereics
class Users(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #because we want to get data based on primary key
    lookup_field = 'pk'         


# use of mixins and genrics needed 2 different classes for pk and non
# based operations, viewset.ViewSet makes it easy to work in single class

class Books(viewsets.ViewSet):
    
    def list(self,request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        book = get_object_or_404(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# use of ViewSet did everything in a single class but we had to write
# a lot of code, so now we'll see ModelViewSet

class DesgnationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

# now we'll work on the blog-comment to implement the nested serialzer
class Blogs(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class Comments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer