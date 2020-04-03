from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(AbstractUser):
    name = models.CharField(max_length=250)
    shipping_addr = models.CharField(max_length=250)
    
    def __str__(self):
        return self.username

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    mediatype = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    photo = models.ImageField(
        height_field=None, width_field=None, max_length=100
    )
    description = models.CharField(max_length=500)
    inventory_count = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    release_year = models.DateField()
    date_posted = models.DateField(auto_now_add=True)


class Payment(models.Model):
    pId = models.AutoField(primary_key=True)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    iId = models.ForeignKey(Item, on_delete=models.CASCADE)
    shipping_addr = models.CharField(max_length=200)
    total_amt = models.DecimalField(max_digits=5, decimal_places=2)
    pDate = models.DateField(auto_now_add=True)

