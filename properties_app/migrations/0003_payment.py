# Generated by Django 4.1.3 on 2022-12-05 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties_app', '0002_room_apartmenturl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=20)),
                ('ref', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=20)),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('booked_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties_app.room')),
            ],
        ),
    ]