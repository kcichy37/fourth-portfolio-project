# Generated by Django 3.2.16 on 2022-11-22 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barber_booking', '0017_alter_querie_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-created_on']},
        ),
    ]