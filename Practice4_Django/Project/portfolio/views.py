from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import mydata

def portfolio(request):
    return HttpResponse("Hello world!")

def contact_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        roll_no = request.POST.get('phone')
        gender = request.POST.get('gender')

        print(first_name)
        print(last_name)
        print(roll_no)
        print(gender)
        # Create and save a new Contact instance
        mydata.objects.create(
            fname=first_name,
            lname=last_name,
            phone=roll_no,
            gender=gender
        )
        return redirect('success')  # Redirect to a success page or another view

    return render(request, 'index.html')

def success(request):
    return HttpResponse("Form submitted successfully!")