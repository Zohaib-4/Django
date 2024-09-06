from django.shortcuts import render
from .models import course_details
from .serializer import CourseSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")