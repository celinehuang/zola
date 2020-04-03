from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ProfileViewSet, ItemViewSet, PaymentViewSet

router = routers.DefaultRouter()
#router.register('profiles', ProfileViewSet)
router.register('items', ItemViewSet)
router.register('payments',PaymentViewSet)

from . import views

urlpatterns = [
    path('', include(router.urls)),
    path('users/', ProfileViewSet.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]