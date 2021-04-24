from django.urls import include, path
from rest_framework import routers

from vaccin.views import VaccinViewSet
from cles_region.views import ClesRegionViewSet, ClesRegionsParSemaine
from cles_departement.views import ClesDepartementViewSet, ClesDepartementsParSemaine
from centre.views import CentreAmbulatoireViewSet

router = routers.DefaultRouter()
router.register(r'centres', CentreAmbulatoireViewSet, basename='centre')
router.register(r'vaccins', VaccinViewSet, basename='vaccin')
router.register(r'departements', ClesDepartementViewSet, basename='departement')
router.register(r'semaine/(?P<semaine>\d+)/departements', ClesDepartementsParSemaine, basename='departement par semaine')
router.register(r'regions', ClesRegionViewSet, basename='region')
router.register(r'semaine/(?P<semaine>\d+)/regions', ClesRegionsParSemaine, basename='region par semaine')

urlpatterns = router.urls