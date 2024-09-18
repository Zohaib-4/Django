from django.contrib import admin
from django.urls import include, path
from course import views
from course.views import Course, Student


urlpatterns = [
    path('admin/', admin.site.urls),

    # get and post
    path('course-info/<int:pk>',Course.as_view()),
    path('course-info/',Course.as_view()),
    # path('course/<int:pk>/enrolled/',views.enrolled_students),
    path('addStudent/',Student.as_view()),
    path('addCourse/',Course.as_view()),
    # path('enrollStudent/',views.enroll_student), 

    #update 
    path('updateCourse/<str:course_id>/update',Course.as_view()),
    path('updateStudent/<str:student_id>/update',Student.as_view),

    #delete
    path('deleteCourse/<str:course_id>/delete',Course.as_view()),
    path('deleteStudent/<str:student_id>/delete',Student.as_view),
] 