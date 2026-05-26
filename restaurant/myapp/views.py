from django.shortcuts import render,redirect
from .models import  tablebooking

def home(request):

    if request.method == 'POST':

        username = request.POST.get('name')
        mobile_number = request.POST.get('phone')
        booking_date = request.POST.get('date')
        booking_time = request.POST.get('timing')
        message = request.POST.get('message')

        user = tablebooking(
            username=username,
            mobile_number=mobile_number,
            booking_date=booking_date,
            booking_time=booking_time,
            message=message
        )

        user.save()

        return redirect('home')

    return render(request, 'index.html')