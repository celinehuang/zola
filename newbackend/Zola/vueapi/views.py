from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status, generics
#from rest_framework.permissions import IsAuthenticated
from .serializers import ProfileSerializer, ItemSerializer, PaymentSerializer
from .models import Profile, Item, Payment
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view, action, authentication_classes
from rest_framework import permissions
#from rest_framework.authentication import TokenAuthentication

#@api_view(['GET'])
#@permission_classes((IsAuthenticated, ))
#@authentication_classes((TokenAuthentication, ))
class ProfileViewSet(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

#@permission_classes((IsAuthenticated, ))
#@authentication_classes((TokenAuthentication, ))
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(methods=['POST'], detail=True)
    def change_description(self, request, pk=None):
        if 'description' in request.data:
            item = Item.objects.get(id=pk)
            newdesc = request.data['description']
            try:    
                item.description = newdesc
                item.save()
                serializer = ItemSerializer(item, many=False)
                response={'message':'desc has been updated', 'result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                console.log('an error occured.')
                response={'message':'error occured'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            console.log('an error occured.')
            response={'message':'error occured'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
