from rest_framework import serializers
from api.models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("id", "identificacion", "nombre", "email", "programa")
        
class ProgramaSerializer(serializers.ModelSerializer):
    
    usuarios = UsuarioSerializer(many=True, read_only=True)
    
    class Meta:
        model = Programa
        fields = ("id", "ficha", "nombre", "codigo", "cupo", "duracion", "jornada", "usuarios")