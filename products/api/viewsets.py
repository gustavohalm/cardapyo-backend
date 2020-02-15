from rest_framework import viewsets
from . import serializers, models


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()

    def get_queryset(self):

        if 'restaurant' in self.request.GET:

            if 'category' in self.request.GET:
                return models.Product.objects.filter(restaurant=self.request.GET['restaurant']).filter(category=self.request.GET['category'])

            return models.Product.objects.filter(restaurant=self.request.GET['restaurant'])

        if 'category' in self.request.GET:
            return models.Product.objects.filter(category=self.request.GET['category'])

        return models.Product.objects.all()