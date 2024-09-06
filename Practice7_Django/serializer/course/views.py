from django.shortcuts import render
from .models import course_details, student_details, enrollment
from .serializer import CourseSerializer, StudentSerializer, EnrollmentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def course_detail(request, pk):
    course = course_details.objects.get(id=pk)
    serializer = CourseSerializer(course)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type="application/json")

def course_list(reqeust):
    course = course_details.objects.all()
    serializer = CourseSerializer(course, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type="application/json")

def enrolled_students(request, pk):
    try:
        course = course_details.objects.get(id=pk)
        enrolled = enrollment.objects.filter(course=course)

        # students = student_details.objects.filter(id__in=enrolled.values_list('student_id', flat=True))
        students = [enrollment.student for enrollment in enrolled]
        
        serializer = StudentSerializer(students, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")
    
    except course_details.DoesNotExist:
        return HttpResponse(status=404)
