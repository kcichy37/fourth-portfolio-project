from django.test import TestCase
from .models import Booking, Query
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
        booking = Booking.objects.create(date='2022-12-03')
        self.assertEquals(booking.date, '2022-12-03')

    def test_time_model(self):
        booking = Booking.objects.create(time='09:00')
        self.assertEquals(booking.time, '09:00')

    def test_barber_model(self):
        booking = Booking.objects.create(barber='Ricardo')
        self.assertEquals(booking.barber, 'Ricardo')

    def test_service_model(self):
        booking = Booking.objects.create(service='haircut')
        self.assertEquals(booking.service, 'haircut')

    def test_email_model(self):
        queries = Query.objects.create(email='email@gmail.com')
        self.assertEquals(queries.email, 'email@gmail.com')

    def test_query_model(self):
        queries = Query.objects.create(query='hello')
        self.assertEquals(queries.query, 'hello')
