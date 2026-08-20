from django.db import models
from django.conf import settings

class CategoriaAviso(models.TextChoices):
    GERAL = 'GERAL', 'Geral'
    ACADEMICO = 'ACADEMICO', 'Acadêmico'
    URGENTE = 'URGENTE', 'Urgente'
    EVENTO = 'EVENTO', 'Evento'

class Aviso(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    categoria = models.CharField(
        max_length=15,
        choices=CategoriaAviso.choices,
        default=CategoriaAviso.GERAL
    )
    is_fixado = models.BooleanField(default=False, help_text="Mantém o aviso no topo do mural.")
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        # Garante que os fixados apareçam primeiro, seguidos pelos mais recentes
        ordering = ['-is_fixado', '-data_criacao']

    def __str__(self):
        return f"{self.titulo} - {self.get_categoria_display()}"