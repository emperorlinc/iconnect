# Generated by Django 3.2.9 on 2021-12-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='display',
            name='blog',
            field=models.TextField(max_length=99999),
        ),
    ]
