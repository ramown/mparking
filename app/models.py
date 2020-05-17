from django.db import models

# Create your models here.
'''
'''
class Area(models.Model):
    nome = models.CharField(max_length=30)
    capacidade = models.IntegerField(max_length=3)
    ativo = models.BooleanField(default=True)


class Evento(models.Model):
    nome = models.CharField(max_length=50)
    data_inicio = models.DateField(null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)
    areas_usadas = modes.ManyToManyField(Area)


