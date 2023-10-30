from django.urls import path
from .views import CourseListView, CourseCreateView, CourseRetrieveView, CourseUpdateView, CourseDeleteView
from .views import UserListView,UserCreateView,UserRetrieveView,UserUpdateView,UserDeleteView
from . import views
from rest_framework import viewsets


urlpatterns = [
    # path('',views.home, name = 'landing_page'),
    # path(' ',UserView.as_view()),
    # path('home',UserView.as_view()),
    # path('course',CourseView.as_view()),
    # path('topic',TopicsView.as_view()),
    # path('course_list',CourseViewSet.as_view())
    
    #here
    path('courses/view',CourseRetrieveView.CourseView()),
    path('courses/',CourseListView.as_view(),name='course_list'),
    path('courses/create/',CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>',CourseRetrieveView.as_view(), name='course_retrive'),
    path('courses/update/<int:pk>',CourseUpdateView.as_view(),name= 'course_update'),
    path('courses/delete/<int:pk>/',CourseDeleteView.as_view(), name='course_delete'),
	#Added here for user
	path('user/create/',UserCreateView.as_view(), name='user_create'),
    path('user/<int:pk>',UserRetrieveView.as_view(), name='user_retrive'),
    path('user/update/<int:pk>',UserUpdateView.as_view(),name= 'user_update'),
    path('user/delete/<int:pk>/',UserDeleteView.as_view(), name='user_delete'),
	

]
