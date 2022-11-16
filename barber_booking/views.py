from django.shortcuts import render
from django.views import generic, View
from .models import Booking


def bookingform(request):

    items = Booking.objects.all()
    context = {
        'items': items
    }

    return render(request, 'index.html', context)