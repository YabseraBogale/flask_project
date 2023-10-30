from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import random
import string

from django.utils.text import slugify
from django.utils import timezone

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    father_name = models.CharField(max_length=100, null=False)
    grandfather_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=False)
    phone_number = models.CharField(max_length=20, blank = False, unique = True )
    password = models.CharField(max_length=50, null=False)
    # password_cofirmation = models.CharField(max_length=50, null=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(default='pexels-pixabay-301926.jpg')
    
    @property
    def get_name(self):
        return self.User.first_name+" "+self.User.father_name+" "+self.User.grandfather_name
    @property
    def get_id(self):
        return self.User.id
    def __str__(self):
        return self.User.first_name
    
class Topics(models.Model):
    topic_name = models.CharField(max_length=100) 
    # slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.topic_name



# class Course(models.Model):
#     content_title = models.CharField(max_length=50, null=False)
#     video = models.FileField(upload_to='media/course_files')
#     description = RichTextField(blank=False, null=False)
#     # image = models.FileField(blank = False, null = False)
#     image = models.ImageField(upload_to='course_images/', default='pexels-pixabay-301926.jpg')
#     thumb = models.FileField(null = True)
#     course_materials = models.FileField(upload_to='media/course_files',null = True, blank=True)
#     learning_outcome = RichTextField(blank = True, null = True)
#     pre_requirement = RichTextField(blank = True, null = True)
#     instructor = models.CharField(max_length = 30, blank = False, null = False)
#     topics = models.ForeignKey(Topics, on_delete=models.SET_NULL, null=True)
#     price = models.FloatField()
#     course_code = models.CharField(max_length=10, unique=True, default='D3F4U1t')


#     def code_genrate(self):
#         code = random.choices(string.ascii_letters + string.digits, n=10)
#         return ''.join(code)

#     def save(self, *args, **kwargs):
#         if not self.code:
#             self.code = self.code_generte()
#         super().save(*args, **kwargs)
        



class Course(models.Model):
    content_title = models.CharField(max_length=50, null=False)
    video = models.FileField(upload_to='media/course_files')
    description = RichTextField(blank=False, null=False)
    image = models.ImageField(upload_to='course_images/', default='pexels-pixabay-301926.jpg')
    thumb = models.ImageField(null=True)
    course_materials = models.FileField(upload_to='media/course_files', null=True, blank=True)
    learning_outcome = RichTextField(blank=True, null=True)
    pre_requirement = RichTextField(blank=True, null=True)
    instructor = models.CharField(max_length=30, blank=False, null=False)
    topics = models.ForeignKey(Topics, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    code = models.CharField(max_length=10, unique=True)

    def code_generate(self):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return code

    def save(self, *args, **kwargs):
        if not self.pk:
            self.code = self.code_generate()
        super().save(*args, **kwargs)







class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)
    

class Featured_course(models.Model):    
    title = models.CharField(max_length=500)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='featured_course')

    def __str__(self):
        return self.Course.title
    
class enrolled_coures(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)    



class Wishlist(models.Model):
    User = models.ForeignKey( User, on_delete=models.CASCADE, related_name='wishlists')
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='wishlist_course')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.User} for the  {self.Course}"



class Questions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    question = RichTextField()

    

class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True, related_name="answer")
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class Certificate(models.Model):
    user = models.ForeignKey( User, on_delete=models.PROTECT, related_name="certificates")
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name="certificates")
    issued_at = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to='qr_codes/')

    def __str__(self):
        return f"{self.User}'s certificate for {self.Course}"


class faq(models.Model):    
    title = models.CharField(max_length=300, blank = False)
    content = RichTextField(blank=False)    




