# Generated by Django 3.2.16 on 2022-11-16 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_booking', '0003_auto_20221116_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('09:00', '09:00'), ('09:45', '09:45'), ('10:30', '10:30'), ('11:15', '11:15'), ('12:00', '12:00'), ('12:45', '12:45'), ('13:30', '13:30'), ('14:15', '14:15'), ('15:00', '15:00'), ('15:45', '15:45'), ('16:30', '16:30')], max_length=10),
        ),
    ]