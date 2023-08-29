from django.db import models

# Create your models here.
class Programa(models.Model):
    
    jornadaChoices = [
        ("Ma","Mañana"),
        ("Ta","Tarde"),
        ("No","Noche"),
        ]
    
    ficha = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    cupo = models.IntegerField()
    duracion = models.IntegerField()
    jornada = models.CharField(max_length=10, choices=jornadaChoices)
    
    def __str__(self) -> str:
        return self.codigo + " - " + self.nombre
    
class Usuario(models.Model):
    identificacion = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    
    programa = models.ForeignKey(Programa, related_name="usuarios", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.identificacion + " - " + self.nombre
    