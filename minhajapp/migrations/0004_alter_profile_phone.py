# Generated by Django 4.0.3 on 2022-03-16 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minhajapp', '0003_alter_profile_phone_alter_profile_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
