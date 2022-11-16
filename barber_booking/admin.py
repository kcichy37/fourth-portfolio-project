from django.contrib import admin
from .models import Booking, Querie


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'date', 'time', 'barber',
                    'created_on')
    search_field = ('full_name', 'barber')
    list_filter = ('barber', 'date')


@admin.register(Querie)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_on', 'query')
