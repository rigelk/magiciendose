from rest_framework import viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ClesDepartementSerializer
from .models import ClesDepartement


class ClesDepartementViewSet(viewsets.ModelViewSet):
    queryset = ClesDepartement.objects.all()
    serializer_class = ClesDepartementSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('=numero_injection', 'vaccin__nom')
    filter_fields = ('date_de_saisie', 'date_de_derniere_modification', 'date_de_validation_provisoire', 'date_de_validation', 'nb_doses')
    ordering_fields = ('date_de_saisie', 'date_de_derniere_modification', 'date_de_validation_provisoire', 'date_de_validation', 'nb_doses')
    ordering = ('-date_de_derniere_modification')


class ClesDepartementsParSemaine(viewsets.ModelViewSet):
    serializer_class = ClesDepartementSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        semaine = self.kwargs.get('semaine')
        return ClesDepartement.objects.filter(semaine_de_vaccination=semaine)