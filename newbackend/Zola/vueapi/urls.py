from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ProfileViewSet, ItemViewSet

# router = routers.DefaultRouter()
# router.register('profiles', ProfileViewSet)
# router.register('items', ItemViewSet)

from . import views

urlpatterns = [
    #path('', include(router.urls)),
    path('users/', ProfileViewSet.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('items/', ItemViewSet)
]