# Generated by Django 5.0.3 on 2024-03-30 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_registration_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='registration_date',
        ),
    ]