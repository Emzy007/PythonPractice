# Generated by Django 5.0.6 on 2024-05-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Skills",
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
                ("emailid", models.CharField(max_length=250)),
                ("skills", models.TextField()),
            ],
        ),
    ]
