from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=254, primary_key=True)
    name = models.CharField(max_length=50)
    shipping_addr = models.CharField(
        max_length=200, blank=True
    )  # users can leave this blank
    password = models.CharField(max_length=100)


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    photo = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100
    )
    description = models.CharField(max_length=500)
    inventory_count = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_posted = models.DateField()


class Payment(models.Model):
    pId = models.IntegerField(primary_key=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    iId = models.ForeignKey(Item, on_delete=models.CASCADE)
    shipping_addr = models.CharField(max_length=200)
    total_amt = models.DecimalField(max_digits=5, decimal_places=2)
    pDate = models.DateField()

