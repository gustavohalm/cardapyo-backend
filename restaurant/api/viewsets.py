from rest_framework import  viewsets
from . import serializers, permissions
from .models import Restaurant
from rest_framework.response import Response


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RestaurantSerializer
    queryset = Restaurant.objects.all()

    def get_queryset(self):

        if 'owner' in self.request.GET:
            return Restaurant.objects.filter(owner= self.request.GET['owner'])

        if 'city' in self.request.GET:
            return Restaurant.objects.filter(city = self.request.GET['city'])
        if 'user' in self.request:
            #TODO REQUEST OWENER ANDF ILTER
            pass
        return Restaurant.objects.all()

    def perform_create(self, serializer):
        #TODO RECOVER OWNER 
        serializer.save()
