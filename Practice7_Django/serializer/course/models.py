
from django.db import models
# from .models import course_details

class course_details(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  instructor = models.CharField(max_length=255)
  duration = models.IntegerField()