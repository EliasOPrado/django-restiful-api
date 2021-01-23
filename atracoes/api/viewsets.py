from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from rest_framework import filters
from .serializers import AtracaoSerializer

class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'nome', 'descricao', 'foto']