from django.shortcuts import render
from .models import course_details
from .serializer import CourseSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def course_detail(request, pk):
    course = course_details.objects.get(id=pk)
    serializer = CourseSerializer(course)
    jason_data = JSONRenderer().render(serializer.data)
    return HttpResponse(jason_data, content_type="application/json")

def course_list(reqeust):
    course = course_details.objects.all()
    serializer = CourseSerializer(course, many=True)
    jason_data = JSONRenderer().render(serializer.data)
    return HttpResponse(jason_data, content_type="application/json")
