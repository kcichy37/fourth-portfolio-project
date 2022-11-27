from django.contrib import admin
from .models import Booking, Query


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Displays data in Admins panel,
    enables admin to search, filter
    and approve data
    """

    list_display = (
        "name",
        "surname",
        "username",
        "service",
        "barber",
        "date",
        "time",
        "created_on",
        "approved",
    )
    search_field = (
        "name",
        "surname",
        "barber",
    )
    list_filter = (
        "barber",
        "date",
    )
    actions = ["confirm_booking"]

    def confirm_booking(self, request, queryset):
        """
        All bookings are set
        to not approved for admin
        to approve on admin panel.
        """
        queryset.update(approved=True)


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
        "email",
        "query",
        "created_on",
    )
