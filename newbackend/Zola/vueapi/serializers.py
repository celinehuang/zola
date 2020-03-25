from rest_framework import serializers
from .models import Profile, Item, Payment
from rest_framework.authtoken.models import Token

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email','name','shipping_addr','username')
        

    # def create(self, validated_data):
    #     user = Profile.objects.create_user_profile(**validated_data)
    #     Token.objects.create(user=user)
    #     return user

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'