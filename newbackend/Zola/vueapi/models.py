from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
class Profile(AbstractUser):
    name = models.CharField(max_length=250)
    shipping_addr = models.CharField(max_length=250)
    profile_pic = models.ImageField(
        height_field=None, width_field=None, max_length=100, upload_to='profilepics', null = True
    )
    def __str__(self):
        return self.username

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    mediatype = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    photo = models.ImageField(
        height_field=None, width_field=None, max_length=100, upload_to='albumart'
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

def validate_content_message(content):
    if (content == "" or content == None or content.isspace()):
        raise ValidationError(
        'Invalid content',
        code = 'invalid',
        params = {
            'content' : content
        }
    )   

class Message(models.Model):
    id = models.AutoField(primary_key = True)
    date = models.DateTimeField(auto_now_add=True, blank = True)
    content = models.TextField(validators=[validate_content_message])
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

