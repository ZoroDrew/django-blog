# Generated by Django 5.0.3 on 2024-03-18 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0002_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]
