from django.db import models

# Create your models here.
class Configuracoes(models.Model):
    usuario = models.CharField(max_length=256)
    mensagens_por_dia = models.IntegerField('Frequencia das mensagens', default=1, blank=True, null=True)

    def __str__(self):
        return 'Configuração do usuario {}: {} mensagens por dia'.format(self.usuario, self.mensagens_por_dia) 

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'

