from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     shipping_addr = models.CharField(max_length=100)

#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()

#     def __str__(self):
#         return self.user.username
class Profile(AbstractUser):
    name = models.CharField(max_length=250)
    shipping_addr = models.CharField(max_length=250)
    
    def __str__(self):
        return self.username

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    mediatype = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    photo = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100
    )
    description = models.CharField(max_length=500)
    inventory_count = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    release_year = models.DateField()
    date_posted = models.DateField()


class Payment(models.Model):
    pId = models.IntegerField(primary_key=True)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    iId = models.ForeignKey(Item, on_delete=models.CASCADE)
    shipping_addr = models.CharField(max_length=200)
    total_amt = models.DecimalField(max_digits=5, decimal_places=2)
    pDate = models.DateField()

