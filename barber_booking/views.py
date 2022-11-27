from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Querie
from .forms import BookingForm, ContactUsForm
from django.contrib.auth.models import User


def index(request):
    # Render the HTML template index.html with the data in the context variable

    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            messages.success(
                request, (
                    """Your query has been sent successfully,
                    we'll email you back shortly."""),
            )
            form.save()
        else:
            form = ContactUsForm()

    return render(request, "index.html", {"form": ContactUsForm})


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
        messages.success(
            request, (
                """Your booking has been successful,
                it's pending confirmation.""")
        )
        return redirect("mybooking")
    else:
        form = BookingForm()

    return render(request, "booking.html", {"form": BookingForm})


@login_required
def mybooking(request):
    """
    Renders users bookings
    on my_booking.html, bookings
    are filtered by users username.
    """
    my_booking = Booking.objects.filter(username=request.user)
    return render(request, "my_booking.html", {"my_booking": my_booking})


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
    if not (booking.username.id == request.user.id):
        return redirect("home")
    else:
        if form.is_valid():
            form.save()
            messages.success(request, ("Booking edited successfully."))
            return redirect("mybooking")

    return render(request, "edit_booking.html", {"booking": booking_id,
                                                 "form": form})


@login_required
def cancelbooking(request, booking_id):
    """
    Enables cancelation
    of users bookings
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if not (booking.username.id == request.user.id):
        return redirect("home")
    else:
        if request.method == "POST":
            booking.delete()
            messages.success(request, ("Booking cancelled successfully."))
            return redirect("mybooking")
            return redirect(mybooking)

        return render(request, "delete_booking.html", {"booking": booking})
