# Generated by Django 3.2.16 on 2022-11-24 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_booking', '0019_alter_booking_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
