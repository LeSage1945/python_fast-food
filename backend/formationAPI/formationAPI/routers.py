
from rest_framework.routers import DefaultRouter
from produit.views import livreViewset, AuteurViewset

router = DefaultRouter()
router.register('livre', livreViewset, basename='livre')
router.register('auteur', AuteurViewset, basename='auteur')
urlpatterns = router.urls