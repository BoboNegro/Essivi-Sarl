from rest_framework import serializers
from .models import Commande, Depot


class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ('__all__')

class DepotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depot
        fields = ('__all__')

