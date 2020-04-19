from django.contrib import admin
from .models import Item, Profile, Payment, Message
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import ProfileCreationForm, ProfileChangeForm

class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile
    list_display = ['username', 'email', 'name', 'shipping_addr']
# Register your models here.
admin.site.register(Item)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Payment)
admin.site.register(Message)