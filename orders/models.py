from django.db import models
from menu.models import MenuItem

# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=300)
    date = models.DateField()
    time = models.TimeField()
    street = models.CharField(max_length=300)
    postal_code = models.IntegerField()
    delivery_status =  models.CharField(max_length=100)

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True,
        related_name = 'order_items'
    )
    order_item = models.BooleanField(default=False)
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.SET_NULL,
        null=True,
        related_name= 'menu_items'
    )
    note = models.TextField(max_length=500)

    # Niels fragen: delivery status, wer gibt ein, wer empffängt ihn, was soll rein?
    # Parameter im Foreign Key (on_delete, null und related_name)
    # Menu Item relates to order item ... ist das so richtig mit dem Foreign Key?