# Generated by Django 4.1.3 on 2022-11-26 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties_app', '0008_remove_booking_status_bookedroom_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Book',
        ),
        migrations.DeleteModel(
            name='BookedRoom',
        ),
    ]
