from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CentreAmbulatoireSerializer
from .models import CentreAmbulatoire


class CentreAmbulatoireViewSet(viewsets.ModelViewSet):
    queryset = CentreAmbulatoire.objects.all()
    serializer_class = CentreAmbulatoireSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('^code_postal', '=gid', 'nom')
    filter_fields = ('gid', 'nom', 'capacite', 'code_postal')
    ordering_fields = ('gid', 'nom', 'capacite', 'code_postal')
    ordering = ('code_postal')