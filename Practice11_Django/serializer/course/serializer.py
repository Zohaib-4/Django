
from rest_framework import serializers
from .models import course_details, enrollment, student_details

class CourseSerializer(serializers.Serializer):
  title = serializers.CharField(max_length=255)
  description = serializers.CharField(max_length=255)
  instructor = serializers.CharField(max_length=255)
  duration = serializers.IntegerField()

  def update(self, instance, validate_data):
    instance.title = validate_data.get('title', instance.title)
    instance.description = validate_data.get('description', instance.description)
    instance.instructor = validate_data.get('instructor', instance.instructor)
    instance.duration = validate_data.get('duration', instance.duration)
    instance.save()
    return instance

  def create(self, validated_data):
    return course_details.objects.create(**validated_data)

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    roll = serializers.IntegerField()
    phone = serializers.IntegerField()
    email = serializers.EmailField()
    

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.roll = validate_data.get('roll', instance.roll)
        instance.phone = validate_data.get('phone', instance.phone)
        instance.email = validate_data.get('email', instance.email)
        instance.save()
        return instance

    def create(self, validated_data):
        return student_details.objects.create(**validated_data)
  
class EnrollmentSerializer(serializers.Serializer):
    course = serializers.PrimaryKeyRelatedField(queryset=course_details.objects.all())
    student = serializers.PrimaryKeyRelatedField(queryset=student_details.objects.all())

    def update(self, instance, validate_data):
        instance.course = validate_data.get('course', instance.course)
        instance.student = validate_data.get('student', instance.student)
        instance.save()
        return instance

    def create(self, validated_data):
        return enrollment.objects.create(**validated_data)
    
