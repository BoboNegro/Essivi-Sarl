from rest_framework import serializers
from .models import Produit, Marque


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ('__all__')

class MarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marque
        fields = ('__all__')

