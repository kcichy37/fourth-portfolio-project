from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponseRedirect
from .models import Booking
from .form import BookingForm
from django.contrib.auth.models import User


def index(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


def bookingform(request):
    form = BookingForm(data=request.POST)
    if form.is_valid():
        form.instance.username = request.user
        form.save()
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': BookingForm})


def mybooking(request):
    my_booking = Booking.objects.filter(username=User.objects.get(username=request.user))
    return render(request, 'mybookings.html',
                  {'my_booking': my_booking})
