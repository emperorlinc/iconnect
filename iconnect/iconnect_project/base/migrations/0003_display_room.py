# Generated by Django 3.2.9 on 2021-12-03 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_display_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='display',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.room'),
        ),
    ]
