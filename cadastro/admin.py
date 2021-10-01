from django.contrib import admin
from .models import *


@admin.register(Materias)
class MateriasAdmin(admin.ModelAdmin):
    list_display = [
        'materia',
        'get_criado',
        'get_atualizado_em',
        'ativo',
    ]
    search_fields = [
        'materia',
    ]


@admin.register(Estudos)
class EstudosAdmin(admin.ModelAdmin):
    list_display = [
        'materia',
        'estudo',
        'get_criado',
        'get_atualizado',
        'ativo',
    ]
    search_fields = [
        'materia',
        'estudo',
    ]
