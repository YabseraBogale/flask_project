from rest_framework import serializers
from .models import User, Course, Topics, Review


class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ('id','first_name', 'father_name', 'grandfather_name',
                 'email', 'phone_number', 'password', 'registration_date' )
        

class CourseSerializer(serializers.ModelSerializer):
     class Meta:
         model = Course
         fields = (
            'id', 'content_title', 'video', 'description', 'course_materials',
            'learning_outcome', 'pre_requirement','instructor','topics','price')        
        



class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = (
            'id', 'topic_name'
        )        

class ReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
         model = Review
         fields = '__all__'

         def get_reviews(self, obj):
             reviews = obj.review_set.all()
             serializer = ReviewSerializer(reviews, many=True)
             return serializer.data        
