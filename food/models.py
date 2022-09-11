from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://img.freepik.com/darmowe-zdjecie/widok-z-gory-pizzy-pepperoni-z-pieczarek-kielbasy-papryka-oliwka-i-kukurydza-na-czarny-drewniany_141793-2158.jpg?w=2000")