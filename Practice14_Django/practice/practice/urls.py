
# ----------- urls .py ----------


from django.contrib import admin
from django.urls import path,include
from jwt import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


router = DefaultRouter()

router.register('practice', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    # path("auth", include('rest_framework.urls')),
    path("gettoken/", TokenObtainPairView.as_view(),name = "token_obtain_pair"),
    path("refreshtoken/", TokenRefreshView.as_view(),name = "token_refresh"),
    path("verifytoken/", TokenVerifyView.as_view(),name = "token_verify"),
 
]

# {
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3MzY2MzgzLCJpYXQiOjE3MjczNjU3ODMsImp0aSI6ImFhNDQyZTVmNjBlNzQzYTQ4NDM3N2Y1MDgxYTI5N2JlIiwidXNlcl9pZCI6MX0.PRwS3R9YNN2t6jo-LJ4aq1VWAnmHCe7iQvnmQPz0Tfo",
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNzk3MDU4MywiaWF0IjoxNzI3MzY1NzgzLCJqdGkiOiI2YjI3ODNmZmQ5MGY0YjE1OGM5OGYwYTdmNmEyZTM4NyIsInVzZXJfaWQiOjF9.Bn1hmk4a5teAWI0pOpMfZTPmZLkGp-kRND2UmAKp2TA"
# }
# ----> Get data 
# http GET http://127.0.0.1:8000/studentApi/


# ----> Get Token 
# http  POST http://127.0.0.1:8000/gettoken/ username="jwt" password="123" 


# ----> verify token  
# http POST http://127.0.0.1:8000/verifytoken/ token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3MzY2MzQ3LCJpYXQiOjE3MjczNjYwNDgsImp0aSI6ImZiNDY5M2Y5ZTVkZTQ0MDY5NGY1ZTY0MmU4NDZhMDdjIiwidXNlcl9pZCI6MX0.t0aKFGKXMjsxrV3vhpbRb00gYf4qpcQi5xwRDWZE4Rk"

# ----> REFRESH token 
# http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNzk3MDg0OCwiaWF0IjoxNzI3MzY2MDQ4LCJqdGkiOiJhNTczZTJmNmRkNTM0NmU3OGIxZGY4NzYzZDExNDBkNiIsInVzZXJfaWQiOjF9.usy1ntIZPnKhDQ8cQkHn-6WI-ldNmHsWYwsiE8OG_KI"



# Get the data after implement token
# http GET http://127.0.0.1:8000/studentApi/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3MzY4NjgzLCJpYXQiOjE3MjczNjY4ODMsImp0aSI6ImZhZWQzMjJmM2Q1MTRmMmJhN2QxOTRlZTdkODlkZjA5IiwidXNlcl9pZCI6MX0.ASqCTe-q5YAtZIdLD3a8mhPcPYamojdC5CdXLvj_Go0'

# ----> post data 
# http -f POST http://127.0.0.1:8000/studentApi/ name=shahbaz roll=101 city=lahore 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3MjYxMDcxLCJpYXQiOjE3MjcyNTgxOTcsImp0aSI6IjdjODliNDUwMmUwMTQ3ZjU4NjVmOTI5YzMyNzlkMzA3IiwidXNlcl9pZCI6MX0.FgwHj9j4NcqB48fDftD3FKZcxYuWiUxD8I7usOoHZDg'

# The -f flag in httpie stands for form-encoded data. It tells httpie to send the request body as application/x-www-form-urlencoded, which is the standard format for HTML form submissions.

# Why Use -f?
# When you use -f, the data is sent in the same format that a typical HTML form would send it. This is useful when you're working with APIs that expect form-encoded data instead of JSON or other formats.
# Without -f, httpie defaults to sending the data as JSON. However, some APIs might expect form-encoded data, especially older APIs or APIs that interact with web forms.


# ----> Put data 
# http -f PUT http://127.0.0.1:8000/studentApi/2/ name=shahbaz roll=101 city=lahore 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3MjYxMDcxLCJpYXQiOjE3MjcyNTgxOTcsImp0aSI6IjdjODliNDUwMmUwMTQ3ZjU4NjVmOTI5YzMyNzlkMzA3IiwidXNlcl9pZCI6MX0.FgwHj9j4NcqB48fDftD3FKZcxYuWiUxD8I7usOoHZDg'


# ----> Delete data 
# http -f DELETE http://127.0.0.1:8000/studentApi/1/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3MjYxMDcxLCJpYXQiOjE3MjcyNTgxOTcsImp0aSI6IjdjODliNDUwMmUwMTQ3ZjU4NjVmOTI5YzMyNzlkMzA3IiwidXNlcl9pZCI6MX0.FgwHj9j4NcqB48fDftD3FKZcxYuWiUxD8I7usOoHZDg'

