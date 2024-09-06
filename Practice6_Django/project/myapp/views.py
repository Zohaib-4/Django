from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

def student_details(request,pk):
    stu = Student.objects.get(id  =pk)
    serializer = StudentSerializer(stu)
    jason_data = JSONRenderer().render(serializer.data)
    return HttpResponse(jason_data , content_type= "application/json")

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu , many= True)
    jason_data = JSONRenderer().render(serializer.data)
    return HttpResponse(jason_data , content_type= "application/json")



