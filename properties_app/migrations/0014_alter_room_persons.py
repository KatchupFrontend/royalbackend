# Generated by Django 4.1.3 on 2022-12-07 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties_app', '0013_alter_room_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='persons',
            field=models.CharField(choices=[('1 in 1', '1 in 1'), ('2 in 1', '2 in 1'), ('3 in 1', '3 in 1'), ('4 in 1', '4 in 1')], max_length=100),
        ),
    ]
