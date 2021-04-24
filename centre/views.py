from rest_framework import viewsets

from .serializers import CentreAmbulatoireSerializer
from .models import CentreAmbulatoire


class CentreAmbulatoireViewSet(viewsets.ModelViewSet):
    queryset = CentreAmbulatoire.objects.all()
    serializer_class = CentreAmbulatoireSerializer
