from django.shortcuts import render
from rest_framework import generics
from api.models import *
from api.serializers import *

# Create your views here.
class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ProgramaList(generics.ListCreateAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer


class ProgramaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer