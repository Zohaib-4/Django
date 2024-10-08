
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),
    path('success/', views.success, name='success')
]
