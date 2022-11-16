from django.db import models


class Booking(models.Model):
    full_name = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    barber = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]


class Querie(models.Model):
    full_name = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    query = models.TextField()

    class Meta:
        ordering = ["created_on"]
