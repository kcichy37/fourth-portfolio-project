from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Booking
from .form import BookingForm
from django.contrib.auth.models import User


def index(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


@login_required
def bookingform(request):
    """
        Posts data to booking form
        and renders the booking page.
    """
    form = BookingForm(data=request.POST)
    if form.is_valid():
        form.instance.username = request.user
        form.save()
        return redirect('mybooking')
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': BookingForm})


@login_required
def mybooking(request):
    """
        Renders users bookings
        on my_booking.html, bookings
        are filtered by users username.
    """
    my_booking = Booking.objects.filter(username=request.user)
    return render(request, 'my_booking.html',
                  {'my_booking': my_booking})


@login_required
def editbooking(request, booking_id):
    """
        Enables editing by fetching
        bookings ID's and creating a
        new form with old information
        for updating.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    form = BookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        form.save()
        return redirect('mybooking')

    return render(request, 'edit_booking.html',
                  {'booking': booking_id,
                   'form': form})


@login_required
def cancelbooking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.username.id == request.user.id
        booking.delete()
        return redirect(mybooking)

    return render(request, 'delete_booking.html', {'booking': booking})
