from rest_framework import viewsets

from .serializers import ClesDepartementSerializer
from .models import ClesDepartement


class ClesDepartementViewSet(viewsets.ModelViewSet):
    queryset = ClesDepartement.objects.all()
    serializer_class = ClesDepartementSerializer