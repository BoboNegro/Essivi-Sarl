from django.db import models
from authentification.models import Utilisateur


class Depot(models.Model):
    code = models.CharField(max_length=128)
    adresse = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

class Commande(models.Model):
    code = models.CharField(max_length=128)
    dateCommande = models.DateTimeField(auto_now_add=True)
    quantite = models.IntegerField
    etat = models.IntegerField
    type = models.CharField(max_length=128)
    details = models.TextField
    client = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    depot = models.ForeignKey(Depot, on_delete=models.CASCADE)





