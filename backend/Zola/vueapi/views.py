from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status, generics, mixins, filters
from .serializers import (
    ProfileSerializer,
    ItemSerializer,
    PaymentSerializer,
    UserSerializer,
    MessageSerializer,
)
from .models import Profile, Item, Payment, Message
from rest_framework.response import Response
from rest_framework.decorators import (
    permission_classes,
    api_view,
    action,
    authentication_classes,
)
from rest_framework import permissions
from django.views.generic.base import TemplateResponseMixin


class ProfileViewSet(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfilePartialUpdateView(
    generics.GenericAPIView, mixins.UpdateModelMixin, TemplateResponseMixin
):
    """
    You just need to provide the field which is to be modified.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    content_type = "multipart/form-data"

    def patch(self, request, *args, **kwargs):
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        return self.partial_update(request, *args, **kwargs)


class ItemViewSet(
    viewsets.ModelViewSet, mixins.UpdateModelMixin, TemplateResponseMixin
):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    content_type = "multipart/form-data"

    def put(self, request, *args, **kwargs):
        print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        return self.partial_update(request, *args, **kwargs)


class ItemSearchView(generics.ListCreateAPIView):
    search_fields = ["artist", "title", "description"]
    filter_backends = (filters.SearchFilter,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
