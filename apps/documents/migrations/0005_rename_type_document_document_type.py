# Generated by Django 5.0.3 on 2024-04-14 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0004_remove_document_owner"),
    ]

    operations = [
        migrations.RenameField(
            model_name="document",
            old_name="type",
            new_name="document_type",
        ),
    ]
