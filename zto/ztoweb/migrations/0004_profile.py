# Generated by Django 5.1.1 on 2024-10-31 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ztoweb', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=8)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
