# Generated by Django 2.2.9 on 2022-03-08 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('um', models.CharField(choices=[('SUPINO_RETO', 'SUPINO_RETO'), ('SUPINO_DECLINADO', 'SUPINO_DECLINADO'), ('CRUCIFIXO_INCLINADO', 'CRUCIFIXO_INCLINADO'), ('PECK-DECK', 'PECK-DECK'), ('CROSSOVER_PEGADA_ALTA', 'CROSSOVER_PEGADA_ALTA'), ('PUXADA_ABERTA_PULLEY', 'PUXADA_ABERTA_PULLEY'), ('PUXADA_FECHADA', 'PUXADA_FECHADA'), ('VOADOR_DORSAL', 'VOADOR_DORSAL'), ('REMADA_ABERTA_TRX', 'REMADA_ABERTA_TRX'), ('PUXADOR_TRIANGULO_NEUTRA', 'PUXADOR_TRIANGULO_NEUTRA'), ('ROSCA_HALTERES', 'ROSCA_HALTERES'), ('ROSCA_MARTELO', 'ROSCA_MARTELO'), ('ROSCA_BARRA_W', 'ROSCA_BARRA_W'), ('ROSCA_BICEPS_TRX', 'ROSCA_BICEPS_TRX'), ('ROSCA_UNILATERAL_CONCENTRADA', 'ROSCA_UNILATERAL_CONCENTRADA'), ('FLEXÃO_DIAMANTE', 'FLEXAO_DIAMANTE'), ('TRÍCEPS_TESTA', 'TRÍCEPS_TESTA'), ('TRÍCEPS_BANCO', 'TRÍCEPS_BANCO'), ('EXTENSÃO_SOB_CABEÇA', 'EXTENSÃO_SOB_CABEÇA'), ('TRICEPS_MAQUINA', 'TRICEPS_MAQUINA'), ('AGACHAMENTO', 'AGACHAMENTO'), ('AGACHAMENTO_MAQUINA', 'AGACHAMENTO_MAQUINA'), ('LEG_PRESS_45º', 'LEG_PRESS_45º'), ('LEG_PRESS_HORIZONTAL', 'LEG_PRESS_HORIZONTAL'), ('STIFF', 'STIFF')], max_length=30)),
                ('dois', models.CharField(choices=[('SUPINO_RETO', 'SUPINO_RETO'), ('SUPINO_DECLINADO', 'SUPINO_DECLINADO'), ('CRUCIFIXO_INCLINADO', 'CRUCIFIXO_INCLINADO'), ('PECK-DECK', 'PECK-DECK'), ('CROSSOVER_PEGADA_ALTA', 'CROSSOVER_PEGADA_ALTA'), ('PUXADA_ABERTA_PULLEY', 'PUXADA_ABERTA_PULLEY'), ('PUXADA_FECHADA', 'PUXADA_FECHADA'), ('VOADOR_DORSAL', 'VOADOR_DORSAL'), ('REMADA_ABERTA_TRX', 'REMADA_ABERTA_TRX'), ('PUXADOR_TRIANGULO_NEUTRA', 'PUXADOR_TRIANGULO_NEUTRA'), ('ROSCA_HALTERES', 'ROSCA_HALTERES'), ('ROSCA_MARTELO', 'ROSCA_MARTELO'), ('ROSCA_BARRA_W', 'ROSCA_BARRA_W'), ('ROSCA_BICEPS_TRX', 'ROSCA_BICEPS_TRX'), ('ROSCA_UNILATERAL_CONCENTRADA', 'ROSCA_UNILATERAL_CONCENTRADA'), ('FLEXÃO_DIAMANTE', 'FLEXAO_DIAMANTE'), ('TRÍCEPS_TESTA', 'TRÍCEPS_TESTA'), ('TRÍCEPS_BANCO', 'TRÍCEPS_BANCO'), ('EXTENSÃO_SOB_CABEÇA', 'EXTENSÃO_SOB_CABEÇA'), ('TRICEPS_MAQUINA', 'TRICEPS_MAQUINA'), ('AGACHAMENTO', 'AGACHAMENTO'), ('AGACHAMENTO_MAQUINA', 'AGACHAMENTO_MAQUINA'), ('LEG_PRESS_45º', 'LEG_PRESS_45º'), ('LEG_PRESS_HORIZONTAL', 'LEG_PRESS_HORIZONTAL'), ('STIFF', 'STIFF')], max_length=30)),
                ('tres', models.CharField(choices=[('SUPINO_RETO', 'SUPINO_RETO'), ('SUPINO_DECLINADO', 'SUPINO_DECLINADO'), ('CRUCIFIXO_INCLINADO', 'CRUCIFIXO_INCLINADO'), ('PECK-DECK', 'PECK-DECK'), ('CROSSOVER_PEGADA_ALTA', 'CROSSOVER_PEGADA_ALTA'), ('PUXADA_ABERTA_PULLEY', 'PUXADA_ABERTA_PULLEY'), ('PUXADA_FECHADA', 'PUXADA_FECHADA'), ('VOADOR_DORSAL', 'VOADOR_DORSAL'), ('REMADA_ABERTA_TRX', 'REMADA_ABERTA_TRX'), ('PUXADOR_TRIANGULO_NEUTRA', 'PUXADOR_TRIANGULO_NEUTRA'), ('ROSCA_HALTERES', 'ROSCA_HALTERES'), ('ROSCA_MARTELO', 'ROSCA_MARTELO'), ('ROSCA_BARRA_W', 'ROSCA_BARRA_W'), ('ROSCA_BICEPS_TRX', 'ROSCA_BICEPS_TRX'), ('ROSCA_UNILATERAL_CONCENTRADA', 'ROSCA_UNILATERAL_CONCENTRADA'), ('FLEXÃO_DIAMANTE', 'FLEXAO_DIAMANTE'), ('TRÍCEPS_TESTA', 'TRÍCEPS_TESTA'), ('TRÍCEPS_BANCO', 'TRÍCEPS_BANCO'), ('EXTENSÃO_SOB_CABEÇA', 'EXTENSÃO_SOB_CABEÇA'), ('TRICEPS_MAQUINA', 'TRICEPS_MAQUINA'), ('AGACHAMENTO', 'AGACHAMENTO'), ('AGACHAMENTO_MAQUINA', 'AGACHAMENTO_MAQUINA'), ('LEG_PRESS_45º', 'LEG_PRESS_45º'), ('LEG_PRESS_HORIZONTAL', 'LEG_PRESS_HORIZONTAL'), ('STIFF', 'STIFF')], max_length=30)),
                ('quatro', models.CharField(choices=[('SUPINO_RETO', 'SUPINO_RETO'), ('SUPINO_DECLINADO', 'SUPINO_DECLINADO'), ('CRUCIFIXO_INCLINADO', 'CRUCIFIXO_INCLINADO'), ('PECK-DECK', 'PECK-DECK'), ('CROSSOVER_PEGADA_ALTA', 'CROSSOVER_PEGADA_ALTA'), ('PUXADA_ABERTA_PULLEY', 'PUXADA_ABERTA_PULLEY'), ('PUXADA_FECHADA', 'PUXADA_FECHADA'), ('VOADOR_DORSAL', 'VOADOR_DORSAL'), ('REMADA_ABERTA_TRX', 'REMADA_ABERTA_TRX'), ('PUXADOR_TRIANGULO_NEUTRA', 'PUXADOR_TRIANGULO_NEUTRA'), ('ROSCA_HALTERES', 'ROSCA_HALTERES'), ('ROSCA_MARTELO', 'ROSCA_MARTELO'), ('ROSCA_BARRA_W', 'ROSCA_BARRA_W'), ('ROSCA_BICEPS_TRX', 'ROSCA_BICEPS_TRX'), ('ROSCA_UNILATERAL_CONCENTRADA', 'ROSCA_UNILATERAL_CONCENTRADA'), ('FLEXÃO_DIAMANTE', 'FLEXAO_DIAMANTE'), ('TRÍCEPS_TESTA', 'TRÍCEPS_TESTA'), ('TRÍCEPS_BANCO', 'TRÍCEPS_BANCO'), ('EXTENSÃO_SOB_CABEÇA', 'EXTENSÃO_SOB_CABEÇA'), ('TRICEPS_MAQUINA', 'TRICEPS_MAQUINA'), ('AGACHAMENTO', 'AGACHAMENTO'), ('AGACHAMENTO_MAQUINA', 'AGACHAMENTO_MAQUINA'), ('LEG_PRESS_45º', 'LEG_PRESS_45º'), ('LEG_PRESS_HORIZONTAL', 'LEG_PRESS_HORIZONTAL'), ('STIFF', 'STIFF')], max_length=30)),
                ('cinco', models.CharField(choices=[('SUPINO_RETO', 'SUPINO_RETO'), ('SUPINO_DECLINADO', 'SUPINO_DECLINADO'), ('CRUCIFIXO_INCLINADO', 'CRUCIFIXO_INCLINADO'), ('PECK-DECK', 'PECK-DECK'), ('CROSSOVER_PEGADA_ALTA', 'CROSSOVER_PEGADA_ALTA'), ('PUXADA_ABERTA_PULLEY', 'PUXADA_ABERTA_PULLEY'), ('PUXADA_FECHADA', 'PUXADA_FECHADA'), ('VOADOR_DORSAL', 'VOADOR_DORSAL'), ('REMADA_ABERTA_TRX', 'REMADA_ABERTA_TRX'), ('PUXADOR_TRIANGULO_NEUTRA', 'PUXADOR_TRIANGULO_NEUTRA'), ('ROSCA_HALTERES', 'ROSCA_HALTERES'), ('ROSCA_MARTELO', 'ROSCA_MARTELO'), ('ROSCA_BARRA_W', 'ROSCA_BARRA_W'), ('ROSCA_BICEPS_TRX', 'ROSCA_BICEPS_TRX'), ('ROSCA_UNILATERAL_CONCENTRADA', 'ROSCA_UNILATERAL_CONCENTRADA'), ('FLEXÃO_DIAMANTE', 'FLEXAO_DIAMANTE'), ('TRÍCEPS_TESTA', 'TRÍCEPS_TESTA'), ('TRÍCEPS_BANCO', 'TRÍCEPS_BANCO'), ('EXTENSÃO_SOB_CABEÇA', 'EXTENSÃO_SOB_CABEÇA'), ('TRICEPS_MAQUINA', 'TRICEPS_MAQUINA'), ('AGACHAMENTO', 'AGACHAMENTO'), ('AGACHAMENTO_MAQUINA', 'AGACHAMENTO_MAQUINA'), ('LEG_PRESS_45º', 'LEG_PRESS_45º'), ('LEG_PRESS_HORIZONTAL', 'LEG_PRESS_HORIZONTAL'), ('STIFF', 'STIFF')], max_length=30)),
                ('seis', models.CharField(blank=True, choices=[('SUPINO_RETO', 'SUPINO_RETO'), ('SUPINO_DECLINADO', 'SUPINO_DECLINADO'), ('CRUCIFIXO_INCLINADO', 'CRUCIFIXO_INCLINADO'), ('PECK-DECK', 'PECK-DECK'), ('CROSSOVER_PEGADA_ALTA', 'CROSSOVER_PEGADA_ALTA'), ('PUXADA_ABERTA_PULLEY', 'PUXADA_ABERTA_PULLEY'), ('PUXADA_FECHADA', 'PUXADA_FECHADA'), ('VOADOR_DORSAL', 'VOADOR_DORSAL'), ('REMADA_ABERTA_TRX', 'REMADA_ABERTA_TRX'), ('PUXADOR_TRIANGULO_NEUTRA', 'PUXADOR_TRIANGULO_NEUTRA'), ('ROSCA_HALTERES', 'ROSCA_HALTERES'), ('ROSCA_MARTELO', 'ROSCA_MARTELO'), ('ROSCA_BARRA_W', 'ROSCA_BARRA_W'), ('ROSCA_BICEPS_TRX', 'ROSCA_BICEPS_TRX'), ('ROSCA_UNILATERAL_CONCENTRADA', 'ROSCA_UNILATERAL_CONCENTRADA'), ('FLEXÃO_DIAMANTE', 'FLEXAO_DIAMANTE'), ('TRÍCEPS_TESTA', 'TRÍCEPS_TESTA'), ('TRÍCEPS_BANCO', 'TRÍCEPS_BANCO'), ('EXTENSÃO_SOB_CABEÇA', 'EXTENSÃO_SOB_CABEÇA'), ('TRICEPS_MAQUINA', 'TRICEPS_MAQUINA'), ('AGACHAMENTO', 'AGACHAMENTO'), ('AGACHAMENTO_MAQUINA', 'AGACHAMENTO_MAQUINA'), ('LEG_PRESS_45º', 'LEG_PRESS_45º'), ('LEG_PRESS_HORIZONTAL', 'LEG_PRESS_HORIZONTAL'), ('STIFF', 'STIFF')], max_length=30)),
                ('sete', models.CharField(blank=True, choices=[('SUPINO_RETO', 'SUPINO_RETO'), ('SUPINO_DECLINADO', 'SUPINO_DECLINADO'), ('CRUCIFIXO_INCLINADO', 'CRUCIFIXO_INCLINADO'), ('PECK-DECK', 'PECK-DECK'), ('CROSSOVER_PEGADA_ALTA', 'CROSSOVER_PEGADA_ALTA'), ('PUXADA_ABERTA_PULLEY', 'PUXADA_ABERTA_PULLEY'), ('PUXADA_FECHADA', 'PUXADA_FECHADA'), ('VOADOR_DORSAL', 'VOADOR_DORSAL'), ('REMADA_ABERTA_TRX', 'REMADA_ABERTA_TRX'), ('PUXADOR_TRIANGULO_NEUTRA', 'PUXADOR_TRIANGULO_NEUTRA'), ('ROSCA_HALTERES', 'ROSCA_HALTERES'), ('ROSCA_MARTELO', 'ROSCA_MARTELO'), ('ROSCA_BARRA_W', 'ROSCA_BARRA_W'), ('ROSCA_BICEPS_TRX', 'ROSCA_BICEPS_TRX'), ('ROSCA_UNILATERAL_CONCENTRADA', 'ROSCA_UNILATERAL_CONCENTRADA'), ('FLEXÃO_DIAMANTE', 'FLEXAO_DIAMANTE'), ('TRÍCEPS_TESTA', 'TRÍCEPS_TESTA'), ('TRÍCEPS_BANCO', 'TRÍCEPS_BANCO'), ('EXTENSÃO_SOB_CABEÇA', 'EXTENSÃO_SOB_CABEÇA'), ('TRICEPS_MAQUINA', 'TRICEPS_MAQUINA'), ('AGACHAMENTO', 'AGACHAMENTO'), ('AGACHAMENTO_MAQUINA', 'AGACHAMENTO_MAQUINA'), ('LEG_PRESS_45º', 'LEG_PRESS_45º'), ('LEG_PRESS_HORIZONTAL', 'LEG_PRESS_HORIZONTAL'), ('STIFF', 'STIFF')], max_length=30)),
                ('oito', models.CharField(blank=True, choices=[('SUPINO_RETO', 'SUPINO_RETO'), ('SUPINO_DECLINADO', 'SUPINO_DECLINADO'), ('CRUCIFIXO_INCLINADO', 'CRUCIFIXO_INCLINADO'), ('PECK-DECK', 'PECK-DECK'), ('CROSSOVER_PEGADA_ALTA', 'CROSSOVER_PEGADA_ALTA'), ('PUXADA_ABERTA_PULLEY', 'PUXADA_ABERTA_PULLEY'), ('PUXADA_FECHADA', 'PUXADA_FECHADA'), ('VOADOR_DORSAL', 'VOADOR_DORSAL'), ('REMADA_ABERTA_TRX', 'REMADA_ABERTA_TRX'), ('PUXADOR_TRIANGULO_NEUTRA', 'PUXADOR_TRIANGULO_NEUTRA'), ('ROSCA_HALTERES', 'ROSCA_HALTERES'), ('ROSCA_MARTELO', 'ROSCA_MARTELO'), ('ROSCA_BARRA_W', 'ROSCA_BARRA_W'), ('ROSCA_BICEPS_TRX', 'ROSCA_BICEPS_TRX'), ('ROSCA_UNILATERAL_CONCENTRADA', 'ROSCA_UNILATERAL_CONCENTRADA'), ('FLEXÃO_DIAMANTE', 'FLEXAO_DIAMANTE'), ('TRÍCEPS_TESTA', 'TRÍCEPS_TESTA'), ('TRÍCEPS_BANCO', 'TRÍCEPS_BANCO'), ('EXTENSÃO_SOB_CABEÇA', 'EXTENSÃO_SOB_CABEÇA'), ('TRICEPS_MAQUINA', 'TRICEPS_MAQUINA'), ('AGACHAMENTO', 'AGACHAMENTO'), ('AGACHAMENTO_MAQUINA', 'AGACHAMENTO_MAQUINA'), ('LEG_PRESS_45º', 'LEG_PRESS_45º'), ('LEG_PRESS_HORIZONTAL', 'LEG_PRESS_HORIZONTAL'), ('STIFF', 'STIFF')], max_length=30)),
                ('nove', models.CharField(blank=True, choices=[('SUPINO_RETO', 'SUPINO_RETO'), ('SUPINO_DECLINADO', 'SUPINO_DECLINADO'), ('CRUCIFIXO_INCLINADO', 'CRUCIFIXO_INCLINADO'), ('PECK-DECK', 'PECK-DECK'), ('CROSSOVER_PEGADA_ALTA', 'CROSSOVER_PEGADA_ALTA'), ('PUXADA_ABERTA_PULLEY', 'PUXADA_ABERTA_PULLEY'), ('PUXADA_FECHADA', 'PUXADA_FECHADA'), ('VOADOR_DORSAL', 'VOADOR_DORSAL'), ('REMADA_ABERTA_TRX', 'REMADA_ABERTA_TRX'), ('PUXADOR_TRIANGULO_NEUTRA', 'PUXADOR_TRIANGULO_NEUTRA'), ('ROSCA_HALTERES', 'ROSCA_HALTERES'), ('ROSCA_MARTELO', 'ROSCA_MARTELO'), ('ROSCA_BARRA_W', 'ROSCA_BARRA_W'), ('ROSCA_BICEPS_TRX', 'ROSCA_BICEPS_TRX'), ('ROSCA_UNILATERAL_CONCENTRADA', 'ROSCA_UNILATERAL_CONCENTRADA'), ('FLEXÃO_DIAMANTE', 'FLEXAO_DIAMANTE'), ('TRÍCEPS_TESTA', 'TRÍCEPS_TESTA'), ('TRÍCEPS_BANCO', 'TRÍCEPS_BANCO'), ('EXTENSÃO_SOB_CABEÇA', 'EXTENSÃO_SOB_CABEÇA'), ('TRICEPS_MAQUINA', 'TRICEPS_MAQUINA'), ('AGACHAMENTO', 'AGACHAMENTO'), ('AGACHAMENTO_MAQUINA', 'AGACHAMENTO_MAQUINA'), ('LEG_PRESS_45º', 'LEG_PRESS_45º'), ('LEG_PRESS_HORIZONTAL', 'LEG_PRESS_HORIZONTAL'), ('STIFF', 'STIFF')], max_length=30)),
                ('dez', models.CharField(blank=True, choices=[('SUPINO_RETO', 'SUPINO_RETO'), ('SUPINO_DECLINADO', 'SUPINO_DECLINADO'), ('CRUCIFIXO_INCLINADO', 'CRUCIFIXO_INCLINADO'), ('PECK-DECK', 'PECK-DECK'), ('CROSSOVER_PEGADA_ALTA', 'CROSSOVER_PEGADA_ALTA'), ('PUXADA_ABERTA_PULLEY', 'PUXADA_ABERTA_PULLEY'), ('PUXADA_FECHADA', 'PUXADA_FECHADA'), ('VOADOR_DORSAL', 'VOADOR_DORSAL'), ('REMADA_ABERTA_TRX', 'REMADA_ABERTA_TRX'), ('PUXADOR_TRIANGULO_NEUTRA', 'PUXADOR_TRIANGULO_NEUTRA'), ('ROSCA_HALTERES', 'ROSCA_HALTERES'), ('ROSCA_MARTELO', 'ROSCA_MARTELO'), ('ROSCA_BARRA_W', 'ROSCA_BARRA_W'), ('ROSCA_BICEPS_TRX', 'ROSCA_BICEPS_TRX'), ('ROSCA_UNILATERAL_CONCENTRADA', 'ROSCA_UNILATERAL_CONCENTRADA'), ('FLEXÃO_DIAMANTE', 'FLEXAO_DIAMANTE'), ('TRÍCEPS_TESTA', 'TRÍCEPS_TESTA'), ('TRÍCEPS_BANCO', 'TRÍCEPS_BANCO'), ('EXTENSÃO_SOB_CABEÇA', 'EXTENSÃO_SOB_CABEÇA'), ('TRICEPS_MAQUINA', 'TRICEPS_MAQUINA'), ('AGACHAMENTO', 'AGACHAMENTO'), ('AGACHAMENTO_MAQUINA', 'AGACHAMENTO_MAQUINA'), ('LEG_PRESS_45º', 'LEG_PRESS_45º'), ('LEG_PRESS_HORIZONTAL', 'LEG_PRESS_HORIZONTAL'), ('STIFF', 'STIFF')], max_length=30)),
                ('aquecimento', models.TextField(blank=True, max_length=350)),
                ('instrutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.professor')),
                ('tr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.aluno')),
            ],
        ),
    ]
