# Generated by Django 5.0 on 2023-12-18 12:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="updated_at",
            new_name="modified_at",
        ),
    ]
