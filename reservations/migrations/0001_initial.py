# Generated by Django 5.0.6 on 2024-06-07 13:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('num_guests', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
