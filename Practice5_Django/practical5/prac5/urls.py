from django.urls import path
from . import views

urlpatterns = [
    path('prac5/', views.prac5, name='prac5'),
    path('login/', views.login, name='login'),
    path('success/', views.success, name='success')

]
