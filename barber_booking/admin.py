from django.contrib import admin
from .models import Booking, Querie
from allauth.account.models import EmailAddress


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'service', 'barber', 'date', 'time', 'created_on',)
    search_field = ('name', 'surname', 'barber',)
    list_filter = ('barber', 'date',)
    actions = ['confirm_booking']

    def confirm_booking(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Querie)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'query', 'created_on',)
