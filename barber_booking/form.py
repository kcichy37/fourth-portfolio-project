from .models import Booking
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
        fields = ('name', 'surname', 'date', 'time', 'barber',
                  'service',)
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'min': datetime.datetime.now().date()})}

    def check_double_booking(self):
        booking_name = self.cleaned_data.get('name')
        for instance in Booking.objects.all():
            if instance.name == Booking.name:
                raise forms.ValidationError('error')
