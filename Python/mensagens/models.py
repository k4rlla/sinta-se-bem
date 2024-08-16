
from django.db import models
from django.utils import timezone

class Mensagem(models.Model):
    data_hora = models.DateTimeField('Data', default=timezone.now)
    texto = models.TextField('Texto')
    rating = models.IntegerField('Rating', default=0, blank=True, null=True)
    visualizada = models.BooleanField(default=False)
    def __str__(self):
        return self.texto
    
    def __repr__(self):
        return 'Mensagem <{}>'.format(self.pk)

    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
