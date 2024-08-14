
# from rest_framework import viewsets
# from .models import Livre, Auteur
# from .serializer import LivreSerializer, AuteurSerializer

# # permission
# from .permissions import Voir_Modifier_Permissions
# from rest_framework import permissions, authentication

# # pagination
# from rest_framework.pagination import PageNumberPagination



# class livreViewsets(viewsets.ModelViewSet):
#     queryset = Livre.objects.all()
#     serializer_class = LivreSerializer
#     permission_classes = [Voir_Modifier_Permissions, permissions.IsAuthenticatedOrReadOnly]
    
#     # pagination_class = PageNumberPagination
#     # page_size = 2

#     # def get_queryset(self):
#     #     queryset = Livre.objects.all()
#     #     # Ajouter des filtres, des recherches, etc.
#     #     return queryset

# class AuterViewsets(viewsets.ModelViewSet):
#     queryset = Auteur.objects.all()
#     serializer_class = AuteurSerializer
#     authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication, authentication.TokenAuthentication]
#     permission_classes = [Voir_Modifier_Permissions, permissions.IsAuthenticated, permissions.IsAdminUser]



from rest_framework import viewsets, permissions, authentication
# recherche
from rest_framework.filters import SearchFilter
# 
from .models import Auteur, Livre
from .serializer import livreSerializer, AuteurSerializer
from .permissions import Permission_Auteur

class livreViewset(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = livreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuteurViewset(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    permission_classes = [Permission_Auteur, permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['nom', 'nationalite']




    
    

