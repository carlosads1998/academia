from django.db import models

UNIDADE_CHOICES= (
    ('ZONA_SUL', 'ZS'),
    ('ZONA_LESTE', 'ZL'),
    ('ZONA_OESTE', 'ZO'),
    ('ZONA_NORTE', 'ZN'),
)

TREINO_CHOICES= (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)

EX_CHOICES=(
    ('SUPINO_RETO', 'SUPINO_RETO'),
    ('SUPINO_DECLINADO', 'SUPINO_DECLINADO'),
    ('CRUCIFIXO_INCLINADO','CRUCIFIXO_INCLINADO'),
    ('PECK-DECK','PECK-DECK'),
    ('CROSSOVER_PEGADA_ALTA', 'CROSSOVER_PEGADA_ALTA'),
    ('PUXADA_ABERTA_PULLEY', 'PUXADA_ABERTA_PULLEY'),
    ('PUXADA_FECHADA', 'PUXADA_FECHADA'),
    ('VOADOR_DORSAL', 'VOADOR_DORSAL'),
    ('REMADA_ABERTA_TRX', 'REMADA_ABERTA_TRX'),
    ('PUXADOR_TRIANGULO_NEUTRA', 'PUXADOR_TRIANGULO_NEUTRA'),
    ('ROSCA_HALTERES', 'ROSCA_HALTERES'),
    ('ROSCA_MARTELO', 'ROSCA_MARTELO'),
    ('ROSCA_BARRA_W', 'ROSCA_BARRA_W'),
    ('ROSCA_BICEPS_TRX', 'ROSCA_BICEPS_TRX'),
    ('ROSCA_UNILATERAL_CONCENTRADA', 'ROSCA_UNILATERAL_CONCENTRADA'),
    ('FLEXÃO_DIAMANTE', 'FLEXAO_DIAMANTE'),
    ('TRÍCEPS_TESTA','TRÍCEPS_TESTA'),
    ('TRÍCEPS_BANCO', 'TRÍCEPS_BANCO'),
    ('EXTENSÃO_SOB_CABEÇA', 'EXTENSÃO_SOB_CABEÇA'),
    ('TRICEPS_MAQUINA', 'TRICEPS_MAQUINA'),
    ('AGACHAMENTO', 'AGACHAMENTO'),
    ('AGACHAMENTO_MAQUINA', 'AGACHAMENTO_MAQUINA'),
    ('LEG_PRESS_45º', 'LEG_PRESS_45º'),
    ('LEG_PRESS_HORIZONTAL', 'LEG_PRESS_HORIZONTAL'),
    ('STIFF', 'STIFF'),
)

class aluno(models.Model):
    nome=models.CharField(max_length=122)
    idade = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    unidade= models.CharField(max_length=11, choices=UNIDADE_CHOICES)
    
    class Meta:
        verbose_name='Aluno'
        verbose_name_plural='Alunos'
    
    def __str__(self):
        return self.nome

class professor(models.Model):
    nome=models.CharField(max_length=122)
    unidade= models.CharField(max_length=11, choices=UNIDADE_CHOICES)
    aluno= models.ForeignKey(aluno, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='Professor'
        verbose_name_plural='Professores'
    
    def __str__(self):
        return self.nome

class treino(models.Model):
    tr = models.ForeignKey(aluno, on_delete=models.CASCADE)
    instrutor= models.ForeignKey(professor, on_delete=models.CASCADE)
    modelo= models.CharField(max_length=1, choices=TREINO_CHOICES)
    um = models.CharField(max_length=30, choices=EX_CHOICES)
    dois= models.CharField(max_length=30, choices=EX_CHOICES)
    tres= models.CharField(max_length=30, choices=EX_CHOICES)
    quatro= models.CharField(max_length=30, choices=EX_CHOICES)
    cinco= models.CharField(max_length=30, choices=EX_CHOICES)
    seis= models.CharField(max_length=30, choices=EX_CHOICES, blank=True)
    sete= models.CharField(max_length=30, choices=EX_CHOICES, blank=True)
    oito= models.CharField(max_length=30, choices=EX_CHOICES, blank=True)
    nove=models.CharField(max_length=30, choices=EX_CHOICES, blank=True)
    dez= models.CharField(max_length=30, choices=EX_CHOICES, blank=True)
    aquecimento= models.TextField(max_length=350, blank=True)