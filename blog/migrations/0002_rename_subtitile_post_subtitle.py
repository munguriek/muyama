# Generated by Django 4.1.4 on 2023-01-03 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="subtitile",
            new_name="subtitle",
        ),
    ]