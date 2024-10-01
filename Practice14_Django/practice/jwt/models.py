
from django.db import models
# from .models import course_details

class course_details(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  instructor = models.CharField(max_length=255)
  duration = models.IntegerField()


class student_details(models.Model):
    name = models.CharField(max_length=255)
    roll = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()

class enrollment(models.Model):
    course = models.ForeignKey(course_details, on_delete=models.CASCADE)
    student = models.ForeignKey(student_details, on_delete=models.CASCADE)