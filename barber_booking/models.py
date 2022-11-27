from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save


# Choice of services for user to pick from.
SERVICE_CHOICES = (
    ("Kids haircut (under 16)", "Kids haircut (under 16)"),
    ("Kids Skin Fade (under 16)", "Kids Skin Fade (under 16)"),
    ("Gents Haircut", "Gents Haircut"),
    ("Gents Haircut & Beard Trim", "Gents Haircut & Beard Trim"),
    ("Gents Skin Fade", "Gents Skin Fade"),
    ("Gents Skin Fade & Beard Trim", "Gents Skin Fade & Beard Trim"),
    ("Buzz Cut (One level all over)", "Buzz Cut (One level all over)"),
    ("Beard Trim", "Beard Trim"),
    ("Senior Cut (Over 65)", "Senior Cut (Over 65)"),
)

# Choice of time for user to pick from.
TIME_CHOICES = (
    ("09:00", "09:00"),
    ("09:45", "09:45"),
    ("10:30", "10:30"),
    ("11:15", "11:15"),
    ("12:00", "12:00"),
    ("12:45", "12:45"),
    ("13:30", "13:30"),
    ("14:15", "14:15"),
    ("15:00", "15:00"),
    ("15:45", "15:45"),
    ("16:30", "16:30"),
)

# Choice of barbers for users to pick from.
BARBER_CHOICES = (
    ("Tom", "Tom"),
    ("Jason", "Jason"),
    ("Harry", "Harry"),
    ("Tony", "Tony"),
    ("Brian", "Brian"),
    ("Ricardo", "Ricardo"),
)


class Booking(models.Model):
    """
    Booking model containing
    all booking information +
    registered user information.
    """

    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    time = models.CharField(max_length=10, choices=TIME_CHOICES)
    barber = models.CharField(max_length=100, choices=BARBER_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES, null=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Ordering of bookings
        in Admins panel.
        """

        ordering = ["-created_on"]


class Querie(models.Model):
    """
    Queries model containing
    basic information a user
    has to provide for Admin.
    """

    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    query = models.TextField()

    class Meta:
        """
        Ordering of bookings
        in Admin panel.
        """

        ordering = ["-created_on"]
