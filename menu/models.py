from django.db import models

# Create your models here.

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

class MenuItem(models.Model):
    catgory = models.ForeignKey(
        MenuCategory, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name = 'items')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    
    