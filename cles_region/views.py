from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ClesRegionSerializer
from .models import ClesRegion


class ClesRegionViewSet(viewsets.ModelViewSet):
    queryset = ClesRegion.objects.all()
    serializer_class = ClesRegionSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('semaine_de_vaccination')
    filter_fields = ('date_de_saisie', 'date_de_derniere_modification', 'semaine_de_vaccination', 'clef_repartition')
    ordering_fields = ('date_de_saisie', 'date_de_derniere_modification', 'semaine_de_vaccination', 'clef_repartition')
    ordering = ('-date_de_derniere_modification')
