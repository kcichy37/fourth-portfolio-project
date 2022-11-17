from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponseRedirect
from .models import Booking
from .form import BookingForm
from allauth.account.forms import SignupForm


def index(request):

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


def bookingform(request):

    form = BookingForm(data=request.POST)
    if form.is_valid():
        form.instance.email = request.user.email
        form.save()
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': BookingForm})
