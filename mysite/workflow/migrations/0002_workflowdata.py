# Generated by Django 4.1.5 on 2023-02-17 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workflow", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkFlowData",
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
                ("task_name", models.CharField(max_length=200)),
                ("start_time", models.DateTimeField(verbose_name="date published")),
                ("end_time", models.DateTimeField(verbose_name="date published")),
                ("completed", models.CharField(max_length=200)),
            ],
        ),
    ]