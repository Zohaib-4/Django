
from rest_framework import serializers
from models import course_details, student_details

class CourseSerializer(serializers.Serializer):
  title = serializers.CharField(max_length=255)
  description = serializers.CharField(max_length=255)
  instructor = serializers.CharField(max_length=255)
  duration = serializers.IntegerField()

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    roll = serializers.IntegerField()
    phone = serializers.IntegerField()
    email = serializers.EmailField()
  
class EnrollmentSerializer(serializers.Serializer):
    course = serializers.PrimaryKeyRelatedField(course_details.objects.all())
    student = serializers.PrimaryKeyRelatedField(student_details.objects.all())
