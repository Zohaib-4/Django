from django.urls import path
from . import views

urlpatterns = [
    path('day1_app/', views.day1_app, name='day1_app'),
]