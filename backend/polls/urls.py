from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('items', ItemViewSet)

from . import views

urlpatterns = [
    path('', include(router.urls)),
]
