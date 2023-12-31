# Generated by Django 4.2.4 on 2023-08-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questgen", "0003_filemodel_easy_filemodel_hard_filemodel_medium_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuestionModel",
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
                ("file", models.FileField(blank=True, null=True, upload_to="store")),
                ("text", models.TextField(default="")),
                ("easy", models.PositiveIntegerField(default=1)),
                ("medium", models.PositiveIntegerField(default=1)),
                ("hard", models.PositiveIntegerField(default=1)),
                ("quest_type", models.TextField(default="boolean")),
            ],
        ),
        migrations.DeleteModel(
            name="FileModel",
        ),
    ]
