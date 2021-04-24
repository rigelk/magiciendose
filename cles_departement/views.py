from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ClesDepartementSerializer
from .models import ClesDepartement


class ClesDepartementViewSet(viewsets.ModelViewSet):
    queryset = ClesDepartement.objects.all()
    serializer_class = ClesDepartementSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('=numero_injection', 'vaccin__nom', '^code_postal', '=gid', 'nom')
    filter_fields = ('date_de_saisie', 'date_de_derniere_modification', 'date_de_validation_provisoire', 'date_de_validation', 'code_postal')
    ordering_fields = ('date_de_saisie', 'date_de_derniere_modification', 'date_de_validation_provisoire', 'date_de_validation')
    ordering = ('-date_de_derniere_modification')


class ClesDepartementsParSemaine(ClesDepartementViewSet):
    def get_queryset(self):
        semaine = self.kwargs.get('semaine')
        return ClesDepartement.objects.filter(semaine_de_vaccination=semaine)
