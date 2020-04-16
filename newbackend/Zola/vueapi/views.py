from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status, generics, mixins
from .serializers import ProfileSerializer, ItemSerializer, PaymentSerializer, UserSerializer
from .models import Profile, Item, Payment
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view, action, authentication_classes
from rest_framework import permissions
from django.views.generic.base import TemplateResponseMixin


class ProfileViewSet(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfilePartialUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin, TemplateResponseMixin):
    '''
    You just need to provide the field which is to be modified.
    '''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    content_type='multipart/form-data'


    def patch(self, request, *args, **kwargs):
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        return self.partial_update(request, *args, **kwargs)

class ItemViewSet(viewsets.ModelViewSet,  mixins.UpdateModelMixin, TemplateResponseMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    content_type = 'multipart/form-data'

    def put(self, request, *args, **kwargs):
        print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
        return self.partial_update(request, *args, **kwargs)
    # @action(methods=['POST'], detail=True)
    # def change_description(self, request, pk=None):
    #     if 'description' in request.data:
    #         item = Item.objects.get(id=pk)
    #         newdesc = request.data['description']
    #         try:    
    #             item.description = newdesc
    #             item.save()
    #             serializer = ItemSerializer(item, many=False)
    #             response={'message':'desc has been updated', 'result':serializer.data}
    #             return Response(response, status=status.HTTP_200_OK)

    #         except:
    #             console.log('an error occured.')
    #             response={'message':'error occured'}
    #             return Response(response, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         console.log('an error occured.')
    #         response={'message':'error occured'}
    #         return Response(response, status=status.HTTP_400_BAD_REQUEST)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
