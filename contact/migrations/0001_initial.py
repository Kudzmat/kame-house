# Generated by Django 4.1.7 on 2023-03-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.TextField(max_length=800)),
                ("email", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
            ],
        ),
    ]
