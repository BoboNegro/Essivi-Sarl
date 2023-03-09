from django.db import models


class Marque(models.Model):
    code = models.CharField(max_length=128)
    libelle = models.CharField(max_length=128)


class Produit(models.Model):
    code = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    libelle = models.CharField(max_length=128)
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE)

