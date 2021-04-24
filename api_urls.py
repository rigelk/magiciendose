from django.urls import include, path
from rest_framework import routers

from vaccin.views import VaccinViewSet
from cles_region.views import ClesRegionViewSet
from cles_departement.views import ClesDepartementViewSet
from centre.views import CentreAmbulatoireViewSet

router = routers.DefaultRouter()
router.register(r'vaccins', VaccinViewSet, basename='vaccin')
router.register(r'cregions', ClesRegionViewSet, basename='region')
router.register(r'cdepartements', ClesDepartementViewSet, basename='departement')
router.register(r'centres', CentreAmbulatoireViewSet, basename='centre')

urlpatterns = router.urls