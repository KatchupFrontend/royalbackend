# Generated by Django 4.1.3 on 2022-12-07 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties_app', '0012_room_apartmenturl_alter_room_persons_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='persons',
            field=models.CharField(choices=[('one in one', '1 in 1'), ('Two in one', '2 in 1'), ('Three in one', '3 in 1'), ('Four in one', '4 in 1')], max_length=100),
        ),
    ]
