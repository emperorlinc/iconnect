# Generated by Django 3.2.9 on 2021-12-03 04:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_display_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
