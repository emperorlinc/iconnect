# Generated by Django 3.2.9 on 2021-12-17 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_profile_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='Nickname', max_length=100),
        ),
    ]
