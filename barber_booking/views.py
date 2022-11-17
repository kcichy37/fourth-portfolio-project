from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponseRedirect
from .models import Booking
from .form import BookingForm


def index(request):

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


def bookingform(request):

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookingForm() 
    return render(request, 'booking.html', {'form': form})
