# Generated by Django 3.2.16 on 2022-11-22 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_booking', '0012_booking_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
