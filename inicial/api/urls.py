from atexit import register
from dis import Instruction
from django.urls import path

from .views import alunoAPIView, alunosAPIView,profAPIView, professorAPIView, treinoAPIView, treinosAPIView
from django.urls import path


urlpatterns = [
    path('alunos/', alunosAPIView.as_view(), name='Alunos'),
    path('aluno/<int:pk>/', alunoAPIView.as_view(), name='Aluno'),
    path('instrutor/', profAPIView.as_view(), name='Instrutor'),
    path('instrutor/<int:pk>/', professorAPIView.as_view(), name='Instrutores'),
    path('treino/', treinoAPIView.as_view(), name='Treino'),
    path('treino/<int:pk>/', treinosAPIView.as_view(), name='Treinos'),
]
