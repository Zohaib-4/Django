from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact_view/', views.contact_view, name='contact_view'),
    path('success/', views.success, name='success'),
]