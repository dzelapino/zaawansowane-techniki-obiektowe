# Generated by Django 5.1.1 on 2024-10-31 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ztoweb', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='login',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]