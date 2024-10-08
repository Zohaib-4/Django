import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import checkdb

# def login(request):
#     error_message = ""
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         print(email)

#         email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#         pass_pattern = r'^(?=.*[!@#$%^&*()_\-+={}[\]|\\:;"\'<>,.?/~`])(?=.*[A-Za-z])(?=.*\d).{8,}$'

#         if not re.match(email_pattern, email) or not re.match(pass_pattern, password) :
#             error_message = "Invalid email format or password format"
#         else:

#             checkdb.objects.create(
#                 email = email,
#                 password = password
#             )
#         return redirect('success')

#     return render(request, 'login.html', {'error_message': error_message})
# @csrf_exempt
def signup(request):
    error_message = ""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        # Debugging output
        print(f"Name: {name}, Email: {email}, Password: {password}")

        # Email and password patterns
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        pass_pattern = r'^(?=.*[!@#$%^&*()_\-+={}[\]|\\:;"\'<>,.?/~`])(?=.*[A-Za-z])(?=.*\d).{8,}$'

        if not re.match(email_pattern, email):
            error_message = "Invalid email format"
        elif not re.match(pass_pattern, password):
            error_message = "Password must be at least 8 characters long, contain letters, numbers, and special characters."
        elif password != confirm_password:
            error_message = "Passwords do not match"
        else:
            # Create a new user in the database
            checkdb.objects.create(
                name=name,
                email=email,
                password=password  # Ideally, you should hash the password before storing it.
            )
            return redirect('success')  # Redirect to a success page or dashboard

    return render(request, 'signup.html', {'error_message': error_message})

def success(request):
    return HttpResponse("All set good to go")