# Generated by Django 3.2.16 on 2022-11-17 13:57

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_booking', '0005_auto_20221116_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name=django.contrib.auth.models.User),
        ),
    ]