from django.shortcuts import render
from rest_framework import generics
from .serializers import alunoSerializer, professorSerializer,treinoSerializer
from .models import aluno, professor, treino
from rest_framework.permissions import IsAuthenticated


class alunosAPIView(generics.ListCreateAPIView):
    queryset= aluno.objects.all()
    serializer_class= alunoSerializer
class alunoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset= aluno.objects.all()
    serializer_class= alunoSerializer

class profAPIView(generics.ListCreateAPIView):
    queryset= professor.objects.all()
    serializer_class= professorSerializer
class professorAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset= professor.objects.all()
    serializer_class= professorSerializer

class treinoAPIView(generics.ListCreateAPIView):
    queryset= treino.objects.all()
    serializer_class = treinoSerializer   
class treinosAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset= treino.objects.all()
    serializer_class = treinoSerializer
