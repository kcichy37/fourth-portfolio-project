# Generated by Django 3.2.16 on 2022-11-24 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("barber_booking", "0022_alter_booking_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="username",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
