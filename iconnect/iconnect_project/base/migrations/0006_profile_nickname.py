# Generated by Django 3.2.9 on 2021-12-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_message_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='some strings', max_length=100),
        ),
    ]
