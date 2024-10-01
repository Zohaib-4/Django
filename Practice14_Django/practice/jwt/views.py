from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import student_details
from .serializer import StudentSerializer

class StudentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = student_details.objects.all()
    serializer_class = StudentSerializer
    

