from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('course.urls')),
    path('admin/', admin.site.urls),
    path('course-info/<int:id>',views.course_details),
    path('course-info/',views.course_list)
]