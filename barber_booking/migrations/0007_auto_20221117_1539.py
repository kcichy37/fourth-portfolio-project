# Generated by Django 3.2.16 on 2022-11-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("barber_booking", "0006_alter_booking_full_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="full_name",
        ),
        migrations.RemoveField(
            model_name="booking",
            name="phone",
        ),
        migrations.AddField(
            model_name="booking",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="booking",
            name="surname",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
