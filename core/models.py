from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco


# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    # Many to many and one to one below
    atracoes = models.ManyToManyField(Atracao)
    Comentarios = models.ManyToManyField(Comentario)
    Avaliacoes = models.ManyToManyField(Avaliacao)
    Endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    def __str__(self):
        return self.nome
