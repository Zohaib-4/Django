import json
from django.shortcuts import render
from .models import course_details, student_details, enrollment
from .serializer import CourseSerializer, StudentSerializer, EnrollmentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

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

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythonData)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type='application/json')
    

@csrf_exempt
def course_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = CourseSerializer(data = pythonData)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type='application/json')
    
@csrf_exempt
def enroll_student(request):
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        pythonData = JSONParser().parse(stream)
        serializer = EnrollmentSerializer(data = pythonData)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def update_student(request, student_roll):
    if request.method == 'PUT':
        try:
            student=student_details.objects.get(roll=student_roll)
        except student_details.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status =404)
        
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({'error': 'Invalid data'}, status=400)
        
        serializer = StudentSerializer(student, data=data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Student updated successfully'}, status= 200)
        else:
            return JsonResponse(serializer.errors, status=400)