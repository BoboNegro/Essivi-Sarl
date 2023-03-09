from django import forms
from .models import Utilisateur


class UtilisateursForms(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ('__all__')