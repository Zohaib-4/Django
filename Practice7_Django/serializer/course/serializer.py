
from rest_framework import serializers
from .models import course_details, enrollment, student_details

class CourseSerializer(serializers.Serializer):
  title = serializers.CharField(max_length=255)
  description = serializers.CharField(max_length=255)
  instructor = serializers.CharField(max_length=255)
  duration = serializers.IntegerField()

  def create(self, validated_data):
    return course_details.objects.create(**validated_data)

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    roll = serializers.IntegerField()
    phone = serializers.IntegerField()
    email = serializers.EmailField()


    def create(self, validated_data):
        return student_details.objects.create(**validated_data)
  
class EnrollmentSerializer(serializers.Serializer):
    course = serializers.PrimaryKeyRelatedField(queryset=course_details.objects.all())
    student = serializers.PrimaryKeyRelatedField(queryset=student_details.objects.all())

    def create(self, validated_data):
        return enrollment.objects.create(**validated_data)
