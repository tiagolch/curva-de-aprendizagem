from django.contrib import admin
from .models import *

@admin.register(Plano_de_aula)
class Plano_de_aula_Admin(admin.ModelAdmin):
    list_display = [
        'materia',
        'estudo',
        'revisao1',
        'revisao2',
        'revisao3',
        'revisao4',
        'ativo'
    ]
    search_fields = [
        'materia',
        'estudo',
    ]
    autocomplete_fields = [
        'materia',
        'estudo',
    ]