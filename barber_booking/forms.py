from .models import Booking, Querie
from django import forms
import datetime


class BookingForm(forms.ModelForm):
    """
    Booking form which
    creates a form template
    that is viewed on booking.html.
    """

    class Meta:
        model = Booking
        fields = (
            "name",
            "surname",
            "date",
            "time",
            "barber",
            "service",
        )
        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date", "min": datetime.datetime.now().date()}
            )
        }


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Querie
        fields = (
            "name",
            "surname",
            "email",
            "query",
        )
