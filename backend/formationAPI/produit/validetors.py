# from rest_framework.serializers import ValidationError
# from .models import Auteur, Livre

# def validation_nom_auteur(value):
#     # Convertir value en minuscules pour la comparaison sensible à la casse
#     nom_lower = value.lower()
    
#     queryset = Auteur.objects.filter(nom__exact=nom_lower)
#     if queryset.exists():
#         #  raise -> est utilisé dans le contexte de la gestion des exceptions 
#         raise ValidationError(f"L'auteur '{value}' existe déjà")
#     return value



from rest_framework.serializers import ValidationError
from .models import Auteur

def validation_nom_auteur(value):
    nom_lower = value.lower()
    queryset = Auteur.objects.filter(nom__exact=nom_lower)
    if queryset.exists():
        raise ValidationError(f"L'auteur '{value}' existe déjà")
    return value