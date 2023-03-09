from rest_framework import serializers
from .models import Utilisateur


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('__all__')

class UtilisateurSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('last_name', 'first_name', 'role', 'email', 'phone_number', 'username', 
                  'dateInscription', 'dateEmbauche', 'gender')
        
class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('email', 'password')