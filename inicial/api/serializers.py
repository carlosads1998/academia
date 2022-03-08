from rest_framework import serializers
from .models import aluno, professor, treino


class alunoSerializer(serializers.ModelSerializer):
    class Meta:
        model= aluno
        fields= (
            'id',
            'nome',
            'idade',
            'peso',
            'altura',
            'unidade',
        )
class professorSerializer(serializers.ModelSerializer):
    class Meta:
        model = professor
        fields = (
            'nome',
            'unidade',
            'aluno',
        )

class treinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = treino
        fields = ( '__all__')