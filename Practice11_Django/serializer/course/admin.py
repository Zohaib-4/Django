from django.contrib import admin
from .models import course_details, student_details, enrollment

# Register your models here.
admin.site.register(course_details)
admin.site.register(student_details)
admin.site.register(enrollment)