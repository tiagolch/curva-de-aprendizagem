from django.db import models
from datetime import timedelta
from cadastro.models import *


class Plano_de_aula(models.Model):
    materia = models.ForeignKey(Materias, on_delete=models.CASCADE, verbose_name='Materia')
    estudo = models.ForeignKey(Estudos, on_delete=models.CASCADE, verbose_name='Estudo')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    observacao = models.TextField(max_length=1000, verbose_name='Observação', blank=True, null=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Plano de aulas'
        verbose_name = 'Plano de aula'

    def __str__(self):
        return f'{self.estudo}'

    def get_criado(self):
        return self.criado_em.strftime("%d/%m/%Y %H:%M")

    def get_atualizado(self):
        return self.atualizado_em.strftime("%d/%m/%Y %H:%M")

    def revisao1(self):
        r = self.criado_em + timedelta(days=1)
        return r.strftime("%d/%m/%Y")

    def revisao2(self):
        r = self.criado_em + timedelta(days=7)
        return r.strftime("%d/%m/%Y")

    def revisao3(self):
        r = self.criado_em + timedelta(days=14)
        return r.strftime("%d/%m/%Y")

    def revisao4(self):
        r = self.criado_em + timedelta(days=30)
        return r.strftime("%d/%m/%Y")
