from django import forms
from .models import User,Course, Review


class user_registration_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'father_name', 'grandfather_name', 'email', 'phone_number', 'password']

class course_creation(forms.ModelForm):
  
    class Meta:
        model = Course
        fields = ['content_title', 'video', 'description', 'image' , 'thumb' , 'course_materials',
                  'learning_outcome', 'pre_requirement', 'instructor' , 'topics' , 'price']
        

class course_view(forms.ModelForm):
  
    class Meta:
        model = Course
        fields = ['content_title', 'video', 'description', 'image' , 'thumb' , 'course_materials',
                  'learning_outcome', 'pre_requirement', 'instructor' , 'topics' , 'price','code']        


class user_login_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
   
    class Meta:
        model = User
        fields = ['email', 'password']


class edit_user_profile(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'father_name', 'grandfather_name', 'email', 'phone_number', 'password', 'profile_pic']


class review_forms(forms.ModelForm):
     class Meta:
         model= Review
         fields = '__all__'
