from rest_framework.serializers import ModelSerializer

from comentarios.api.serializers import ComentarioSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    Avaliacoes = AvaliacaoSerializer(many=True)
    Comentarios = ComentarioSerializer(many=True)
    atracoes = AtracaoSerializer(many=True)
    Endereco = EnderecoSerializer()

    class Meta:
        model = PontoTuristico
        fields = ['id',
                  'nome',
                  'descricao',
                  'aprovado',
                  'foto',
                  # Foreign Keys/ManyToMany
                  'atracoes',
                  'Comentarios',
                  'Avaliacoes',
                  'Endereco',
                  ]
