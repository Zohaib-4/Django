from django.contrib import admin
from django.urls import path,include
from myapp import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from myapp.auth import CustomAuthToken


router = DefaultRouter()

router.register('studentApi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("auth", include('rest_framework.urls')),
    # path("gettoken/", obtain_auth_token),
    path("gettoken/", CustomAuthToken.as_view()),
]



# 1. First Method
# create the token from the admin panel

# 2. Second Method
# create the token through the terminal

# ----> python3 manage.py drf_create_token token

# 3. Third Method
# create the endpoint in the url.py file and then hit the endpoint

# 1.install the httpie
# pip install httpie

# 2. in terminal send request to the endpoint
# http POST http://127.0.0.1:8000/gettoken/ username="user1" password="pakistan189"
# http POST http://127.0.0.1:8000/gettoken/ username="user2" password="pakistan189"

# 4. Fourth Method
# create our custom auth class get from the drf documentation

# 4. FIFTH Method
# create signal method in model whenever user created token automatically generate.


# 40dc1bda0c19c2268a67db6eeaa790f61d0ec0f9 (Super user token)


# ----> Get data 
# http GET http://127.0.0.1:8000/studentApi/ "Authorization:Token 96469bace3de13b7f4b2ec888e05b6636a52b513"


# ----> post data 
# http -f POST http://127.0.0.1:8000/studentApi/ name=rohan roll=102 city=lahore "Authorization:Token 40dc1bda0c19c2268a67db6eeaa790f61d0ec0f9"

# The -f flag in httpie stands for form-encoded data. It tells httpie to send the request body as application/x-www-form-urlencoded, which is the standard format for HTML form submissions.

# Why Use -f?
# When you use -f, the data is sent in the same format that a typical HTML form would send it. This is useful when you're working with APIs that expect form-encoded data instead of JSON or other formats.
# Without -f, httpie defaults to sending the data as JSON. However, some APIs might expect form-encoded data, especially older APIs or APIs that interact with web forms.


# ----> Put data 
# http PUT http://127.0.0.1:8000/studentApi/4/ name=rohan roll=102 city=lahore "Authorization:Token 40dc1bda0c19c2268a67db6eeaa790f61d0ec0f9"


# ----> Delete data 
# http DELETE http://127.0.0.1:8000/studentApi/4/ name=rohan roll=102 city=lahore "Authorization:Token 40dc1bda0c19c2268a67db6eeaa790f61d0ec0f9"