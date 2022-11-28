from django.test import TestCase
from .forms import BookingForm, ContactUsForm


class TestBookingForm(TestCase):
    def test_booking_form_name_is_required(self):
        form = BookingForm({"name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors.keys())
        self.assertEqual(form.errors["name"][0], "This field is required.")

    def test_booking_form__surname_is_required(self):
        form = BookingForm({"surname": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("surname", form.errors.keys())
        self.assertEqual(form.errors["surname"][0], "This field is required.")

    def test_booking_form_date_is_required(self):
        form = BookingForm({"date": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("date", form.errors.keys())
        self.assertEqual(form.errors["date"][0], "This field is required.")

    def test_booking_form_time_is_required(self):
        form = BookingForm({"time": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("time", form.errors.keys())
        self.assertEqual(form.errors["time"][0], "This field is required.")

    def test_booking_form_barber_is_required(self):
        form = BookingForm({"barber": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("barber", form.errors.keys())
        self.assertEqual(form.errors["barber"][0], "This field is required.")

    def test_booking_form_service_is_required(self):
        form = BookingForm({"service": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("service", form.errors.keys())
        self.assertEqual(form.errors["service"][0], "This field is required.")

    def test_field_are_explicit_in_form_metaclass(self):
        form = BookingForm()
        self.assertEqual(
            form.Meta.fields, ("name", "surname", "date",
                               "time", "barber", "service")
        )


class TestContactUsForm(TestCase):
    def test_contact_us_name_is_required(self):
        form = ContactUsForm({"name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors.keys())
        self.assertEqual(form.errors["name"][0], "This field is required.")

    def test_contact_us_surname_is_required(self):
        form = ContactUsForm({"surname": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("surname", form.errors.keys())
        self.assertEqual(form.errors["surname"][0], "This field is required.")

    def test_contact_us_email_is_required(self):
        form = ContactUsForm({"email": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors.keys())
        self.assertEqual(form.errors["email"][0], "This field is required.")

    def test_contact_us_query_is_required(self):
        form = ContactUsForm({"query": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("query", form.errors.keys())
        self.assertEqual(form.errors["query"][0], "This field is required.")

    def test_field_are_explicit_in_form_metaclass(self):
        form = ContactUsForm()
        self.assertEqual(form.Meta.fields,
                         ("name", "surname", "email", "query"))
