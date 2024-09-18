import json
from django.shortcuts import render
from django.views import View
from .models import course_details, student_details, enrollment
from .serializer import CourseSerializer, StudentSerializer, EnrollmentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class Course(View):
    def get(self, request, pk):
        course = course_details.objects.get(id=pk)
        serializer = CourseSerializer(course)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")
    
    def post(self, request):
        data = request.body
        stream = io.BytesIO(data)
        pythonData = JSONParser().parse(stream)
        serializer = CourseSerializer(data = pythonData)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, course_id):
        try:
            course = course_details.objects.get(id=course_id)
        except course_details.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)
        
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({'error': 'Invalid data'}, status=400)
        
        serializer = CourseSerializer(course, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Course updated successfully'}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

    def delete(self, request, course_id):
        try:
            course = course_details.objects.get(id=course_id)
        except course_details.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)
        
        
        course.delete()
        return JsonResponse({'message': 'Course deleted successfully'}, status=200)
    
class Student(View):
    def get(self, request, student_roll):
        student = student_details.objects.get(roll=student_roll)
        serializer = StudentSerializer(student)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request):
        data = request.body
        stream = io.BytesIO(data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythonData)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, student_roll):
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
    
    def delete(self, request, student_roll):
        try:
            student = student_details.objects.get(roll=student_roll)
        except student_details.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        
        student.delete()
        return JsonResponse({'message': 'Student deleted successfully'}, status=200)

# def course_detail(request, pk):
#     course = course_details.objects.get(id=pk)
#     serializer = CourseSerializer(course)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type="application/json")

# def course_list(reqeust):
#     course = course_details.objects.all()
#     serializer = CourseSerializer(course, many=True)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type="application/json")

# def enrolled_students(request, pk):
#     try:
#         course = course_details.objects.get(id=pk)
#         enrolled = enrollment.objects.filter(course=course)

#         # students = student_details.objects.filter(id__in=enrolled.values_list('student_id', flat=True))
#         students = [enrollment.student for enrollment in enrolled]
        
#         serializer = StudentSerializer(students, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type="application/json")
    
#     except course_details.DoesNotExist:
#         return HttpResponse(status=404)

# @csrf_exempt
# def student_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythonData = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = pythonData)

#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
        
#         json_data = JSONRenderer().render(serializer.error_messages)
#         return HttpResponse(json_data, content_type='application/json')
    

# @csrf_exempt
# def course_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythonData = JSONParser().parse(stream)
#         serializer = CourseSerializer(data = pythonData)

#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
        
#         json_data = JSONRenderer().render(serializer.error_messages)
#         return HttpResponse(json_data, content_type='application/json')
    
# @csrf_exempt
# def enroll_student(request):
#     if request.method == 'POST':
#         data = request.body
#         stream = io.BytesIO(data)
#         pythonData = JSONParser().parse(stream)
#         serializer = EnrollmentSerializer(data = pythonData)

#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
        
#         json_data = JSONRenderer().render(serializer.error_messages)
#         return HttpResponse(json_data, content_type='application/json')

# @csrf_exempt
# def student_update(request, student_roll):
#     if request.method == 'PUT':
#         try:
#             student=student_details.objects.get(roll=student_roll)
#         except student_details.DoesNotExist:
#             return JsonResponse({'error': 'Student not found'}, status =404)
        
#         try:
#             data = json.loads(request.body)
#         except:
#             return JsonResponse({'error': 'Invalid data'}, status=400)
        
#         serializer = StudentSerializer(student, data=data, partial = True)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'message': 'Student updated successfully'}, status= 200)
#         else:
#             return JsonResponse(serializer.errors, status=400)

# @csrf_exempt  
# def course_update(request, course_id):
#     try:
#         course = course_details.objects.get(id=course_id)
#     except course_details.DoesNotExist:
#         return JsonResponse({'error': 'Course not found'}, status=404)
    
#     if request.method == 'PUT':
#         try:
#             data = json.loads(request.body)
#         except:
#             return JsonResponse({'error': 'Invalid data'}, status=400)
        
#         serializer = CourseSerializer(course, data=data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'message': 'Course updated successfully'}, status=200)
#         else:
#             return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def course_delete(request, course_id):
#     if request.method == 'DELETE':
#         try:
#             course = course_details.objects.get(id=course_id)
#         except course_details.DoesNotExist:
#             return JsonResponse({'error': 'Course not found'}, status=404)
        
        
#         course.delete()
#         return JsonResponse({'message': 'Course deleted successfully'}, status=200)

#     return HttpResponse(status=405)

# @csrf_exempt
# def student_delete(request, student_roll):
#     if request.method == 'DELETE':
#         try:
#             student = student_details.objects.get(roll=student_roll)
#         except student_details.DoesNotExist:
#             return JsonResponse({'error': 'Student not found'}, status=404)
        
#         student.delete()
#         return JsonResponse({'message': 'Student deleted successfully'}, status=200)

#     return HttpResponse(status=405)

