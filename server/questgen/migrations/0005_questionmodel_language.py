# Generated by Django 4.2.4 on 2023-08-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questgen', '0004_questionmodel_delete_filemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionmodel',
            name='language',
            field=models.TextField(default='english'),
        ),
    ]
