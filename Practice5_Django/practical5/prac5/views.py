from django.shortcuts import render
from django.http import HttpResponse
from .models import checkdb

def prac5(request):
    return HttpResponse("This is Practical#5 of Django")

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print(email)
        
        checkdb.objects.create(
            email = email,
            password = password
        )

    return render(request, 'login.html')

def success(request):
    return HttpResponse("All set good to go")