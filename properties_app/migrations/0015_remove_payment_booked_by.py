# Generated by Django 4.1.3 on 2022-12-11 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties_app', '0014_alter_room_persons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='booked_by',
        ),
    ]
