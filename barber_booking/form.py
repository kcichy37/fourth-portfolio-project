from .models import Booking
from django import forms
import datetime


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date', 'time', 'barber',
                  'service',)
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'min': datetime.datetime.now().date()}),
        }
