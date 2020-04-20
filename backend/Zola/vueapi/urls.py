from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import (
    ProfileViewSet,
    ItemViewSet,
    PaymentViewSet,
    ProfilePartialUpdateView,
    MessageViewSet,
    ItemSearchView,
)

router = routers.DefaultRouter()
# router.register('profiles', ProfileViewSet)
router.register("items", ItemViewSet)
router.register("payments", PaymentViewSet)
router.register("messages", MessageViewSet)

from . import views

urlpatterns = [
    path("", include(router.urls)),
    path("itemsearch/", ItemSearchView.as_view()),
    path("users/", ProfileViewSet.as_view()),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("partialupdate/<int:pk>/", ProfilePartialUpdateView.as_view()),
]
