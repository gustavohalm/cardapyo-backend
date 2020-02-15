from django.db import models
# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    cnpj = models.CharField(max_length=15, blank=True, null=True)
    cep = models.CharField(max_length=8)
    city = models.CharField(max_length=64)
    neighborhood = models.CharField(max_length=64)
    street = models.CharField(max_length=128)
    number = models.CharField(max_length=16)
    owner = models.CharField(max_length=256)

    def __str__(self):
        return self.name
