from rest_framework.fields import SerializerMethodField
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
    descricao_completa = SerializerMethodField()

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
                  # Incluido do SerializerMethodField
                  'descricao_completa',
                  ]

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
