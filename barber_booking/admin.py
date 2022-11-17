from django.contrib import admin
from .models import Booking, Querie


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'service', 'barber', 'date', 'time')
    search_field = ('full_name', 'barber')
    list_filter = ('barber', 'date')
    actions = ['confirm_booking']


@admin.register(Querie)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_on', 'query')
