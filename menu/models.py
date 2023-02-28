from django.db import models

# Create your models here.
class Menu(models.Model):
    itemName = models.CharField(max_length=200)
    itemPrice = models.IntegerField()
    quantity = models.IntegerField()