from django.contrib import admin
from .models import Livre, Auteur

admin.site.register(Livre)
admin.site.register(Auteur)