# Generated by Django 5.0.3 on 2024-04-13 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_notificationsettings"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="notificationsettings",
            options={
                "verbose_name": "notification_settings",
                "verbose_name_plural": "notification_settings",
            },
        ),
        migrations.AlterModelTable(
            name="notificationsettings",
            table="notification_settings",
        ),
    ]
