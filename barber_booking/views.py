from django.shortcuts import render, redirect
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


def editbooking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    form = BookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        form.save()
        return redirect('mybooking')

    return render(request, 'edit_booking.html',
                  {'booking': booking_id,
                   'form': form})


def deletebooking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.delete()
    return redirect('mybooking')
