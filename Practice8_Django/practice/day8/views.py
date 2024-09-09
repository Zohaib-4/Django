from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Student
from serializers import StudentSerializer

# Create your views here.


def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentStudent(data = pythonData)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HTTPResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.error_messages)
        return HTTPResponse(json_data, content_type='application/json')