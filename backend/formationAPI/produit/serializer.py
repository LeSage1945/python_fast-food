
from rest_framework import serializers, validators
from .models import Auteur, Livre
from .validetors import validation_nom_auteur


class livreSerializer(serializers.ModelSerializer):
    nomAuteur = serializers.CharField(source='auteur')
    class Meta:
        model = Livre
        fields = ('nomAuteur', 'titre')

class AuteurSerializer(serializers.ModelSerializer):
    nom = serializers.CharField(validators = [validation_nom_auteur])
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Auteur
        fields = ('user_id', 'user', 'nom', 'nationalite')
