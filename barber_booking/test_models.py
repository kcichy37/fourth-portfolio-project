from django.test import TestCase
from .models import Booking, Querie
from django.contrib.auth.models import User


class TestModels(TestCase):

    def test_user_register(self):
        test_user = User.objects.create(
            password='Apple', username='Banana'
        )

    def test_name_model(self):
        booking = Booking.objects.create(name='Gary')
        self.assertEquals(booking.name, 'Gary')

    def test_surname_model(self):
        booking = Booking.objects.create(surname='Rogers')
        self.assertEquals(booking.surname, 'Rogers')

    def test_date_model(self):
        booking = Booking.objects.create(date='')
        self.assertEquals(booking.date, '')
