from django.db import models



class Materias(models.Model):
    materia = models.CharField(max_length=30, verbose_name='Materia',  unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Materias'
        verbose_name = 'Materia'

    def __str__(self):
        return self.materia

    def get_criado(self):
        return self.criado_em.strftime("%d/%m/%Y %H:%M")

    def get_atualizado_em(self):
        return self.atualizado_em.strftime("%d/%m/%Y %H:%M")


class Estudos(models.Model):
    materia = models.ForeignKey(Materias, on_delete=models.DO_NOTHING, verbose_name='Materia')
    estudo = models.CharField(max_length=100, verbose_name='Estudo')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Estudos'
        verbose_name = 'Estudo'

    def __str__(self):
        return self.estudo

    def materia_(self):
        return f'{self.materia}'

    def get_criado(self):
        return self.criado_em.strftime("%d/%m/%Y %H:%M")

    def get_atualizado(self):
        return self.atualizado_em.strftime("%d/%m/%Y %H:%M")
