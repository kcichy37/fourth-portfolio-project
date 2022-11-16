from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'date', 'time', 'barber',
                    'created_on')
    search_field = ('full_name', 'barber')
    list_filter = ('barber', 'date')
