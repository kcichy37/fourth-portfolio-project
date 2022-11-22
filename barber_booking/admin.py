from django.contrib import admin
from .models import Booking, Querie


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'username', 'service', 'barber', 'date',
                    'time', 'created_on', 'approved')
    search_field = ('name', 'surname', 'barber',)
    list_filter = ('barber', 'date',)
    actions = ['confirm_booking']

    def confirm_booking(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Querie)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'query', 'created_on',)
