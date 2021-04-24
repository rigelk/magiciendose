from rest_framework import viewsets

from .serializers import VaccinSerializer
from .models import Vaccin


class VaccinViewSet(viewsets.ModelViewSet):
    queryset = Vaccin.objects.all().order_by('nom')
    serializer_class = VaccinSerializer
