from rest_framework import serializers
from .models import Profile, Item, Payment
from rest_framework.authtoken.models import Token
from rest_auth.registration.serializers import RegisterSerializer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email','name','shipping_addr','username')
        

    # def create(self, validated_data):
    #     user = Profile.objects.create_user_profile(**validated_data)
    #     Token.objects.create(user=user)
    #     return user

class RegisterProfileSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=250)
    shipping_addr = serializers.CharField(max_length=250)
    def get_cleaned_data(self):
            data_dict = super().get_cleaned_data()
            data_dict['name'] = self.validated_data.get('name', '')
            data_dict['shipping_addr'] = self.validated_data.get('shipping_addr','')
            return data_dict

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'