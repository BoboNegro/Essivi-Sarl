import uuid
from django.db import models

class Utilisateur(models.Model):
    code = models.UUIDField(default=None, max_length=128, primary_key=True)
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    role = models.CharField(max_length=128, default=None)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=30, default=None)
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    isPasswordSet = models.BooleanField(default=True)
    dateInscription = models.DateTimeField(default=None)
    dateEmbauche = models.DateTimeField(default=None)
    gender = models.CharField(max_length=128)
    actif = models.BooleanField(default=True)