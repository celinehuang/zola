from django.contrib import admin

# Register your models here.
from .models import User, Item

admin.site.register(Item)
admin.site.register(User)
