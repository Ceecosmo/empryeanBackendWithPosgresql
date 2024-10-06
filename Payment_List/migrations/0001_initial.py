# Generated by Django 5.1 on 2024-08-22 00:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                ("name", models.CharField(max_length=100)),
                ("ref", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=30)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("course_name", models.CharField(max_length=500)),
                (
                    "course_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("creditors_address", models.CharField(max_length=1000)),
                ("message", models.TextField(blank=True, null=True)),
                ("verified", models.BooleanField(default=False)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ("-date_created",),
            },
        ),
    ]
