from rest_framework import serializers
from . import models


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Restaurant
        fields = '__all__'
        read_only_fields = ['id', owner]
