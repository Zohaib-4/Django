from django.contrib import admin
from django.urls import include, path
from jwt import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course-info/<int:pk>',views.course_detail),
    path('course-info/',views.course_list),
    path('course/<int:pk>/enrolled/',views.enrolled_students),
    path('addStudent/',views.student_create),
    path('addCourse/',views.course_create),
    path('enrollStudent/',views.enroll_student)

] 