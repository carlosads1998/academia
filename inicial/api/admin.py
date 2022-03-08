from django.contrib import admin
from .models import aluno, professor, treino

@admin.register(aluno)
class alunoAdmin(admin.ModelAdmin):
    list_display= ('nome', 'idade', 'peso', 'altura', 'unidade')

@admin.register(professor)
class professorAdmin(admin.ModelAdmin):
    list_display= ('nome', 'unidade', 'aluno')

@admin.register(treino)
class treinoAdmin(admin.ModelAdmin):
    list_display=('tr', 'instrutor', 'modelo', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'aquecimento')