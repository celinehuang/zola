from rest_framework import serializers
from .models import Profile, Item, Payment, Message
from rest_framework.authtoken.models import Token
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from rest_auth.serializers import UserDetailsSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("username", "email", "name", "shipping_addr", "profile_pic", "id")


class LoginSerializer(RestAuthLoginSerializer):
    email = None


class RegisterProfileSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=250)
    shipping_addr = serializers.CharField(max_length=250)
    profile_pic = serializers.ImageField(required=False)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict["name"] = self.validated_data.get("name", "")
        data_dict["shipping_addr"] = self.validated_data.get("shipping_addr", "")
        data_dict["profile_pic"] = self.validated_data.get("profile_pic", "")
        return data_dict


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("username", "email", "name", "shipping_addr", "profile_pic", "id")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "content", "user", "date"]
