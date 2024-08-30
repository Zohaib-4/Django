from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import checkdb
import re

def prac5(request):
    return HttpResponse("This is Practical#5 of Django")

def login(request):
    error_message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email)

        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        pass_pattern = r'^(?=.*[!@#$%^&*()_\-+={}[\]|\\:;"\'<>,.?/~`])(?=.*[A-Za-z])(?=.*\d).{8,}$'

        if not re.match(email_pattern, email) or not re.match(pass_pattern, password) :
            error_message = "Invalid email format or password format"
        else:

            checkdb.objects.create(
                email = email,
                password = password
            )
        return redirect('success')

    return render(request, 'login.html', {'error_message': error_message})

def success(request):
    return HttpResponse("All set good to go")