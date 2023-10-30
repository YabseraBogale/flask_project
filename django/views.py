from django.shortcuts import render,redirect
from rest_framework import generics,viewsets
from .serializers import UserSerializer, CourseSerializer,TopicsSerializer
from .models import User, Course, Topics
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .forms import user_registration_form,course_view
from rest_framework import generics
# Create your views here.



class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseCreateView(generics.CreateAPIView):
    serializer_class = CourseSerializer

class CourseRetrieveView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def CourseView(self):
        data =.Course.objects.values_list(
                            'content_title','video','description','image','thumb',
                            'course_materials','learning_outcome','pre_requirement',
                            'instructor','topics','price')
        return data
            
        

class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



















