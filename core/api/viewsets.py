from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from core.models import PontoTuristico
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.authtoken.models import Token
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    # permission_classes = (IsAuthenticated,) <<== uncomment
    # permission_classes = (IsAdmin,) will allow this view only for the Admins
    # authentication_classes =( TokenAuthentication,)
    # authentication_classes = [SessionAuthentication, BasicAuthentication] <== uncomment

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset .objects.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.objects.filter(descricao=descricao)

        return queryset