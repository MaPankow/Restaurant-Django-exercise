from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
# Reservations have a name, date and time and number of guests.

class Reservation(models.Model):
    name = models.CharField(max_length=300)
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(30),
            MinValueValidator(1),
        ]
    )