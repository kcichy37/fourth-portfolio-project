from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .models import Booking


def index(request):

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


def bookingform(request):

    items = Booking.objects.all()
    context = {
        'items': items
    }

    return render(request, 'booking.html', context)
