from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
'''
class Area(models.Model):
    nome = models.CharField(max_length=30)
    capacidade = models.IntegerField()
    ativo = models.BooleanField(default=True)


class Evento(models.Model):
    nome = models.CharField(max_length=50)
    data_inicio = models.DateField(null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)
    areas_usadas = models.ManyToManyField(Area)

class Pessoa(models.Model):
	nome = models.CharField(max_length=50)


class Funcionario(Pessoa):
	matricula = models.CharField(max_length=15)
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class Proprietario(Pessoa):
	TIPOS_PROPS = (
		(0, 'ALUNO'), 
		(1, 'PROFESSORES'), 
		(2, 'ADMINISTRATIVO'), 
		(3, 'VISITANTES'),) 
	tipo = models.IntegerField(choices=TIPOS_PROPS)

class Ocorrencia(models.Model):
	TIPOS_OCORRENCIAS = (
		(0, 'FURTO'), 
		(1, 'SINISTRO'), 
		(2, 'ESTACIONAMENTO INDEVIDO'), 
		(3, 'AVARIA'), 
		(4, 'INUNDAÇÃO'), 
		(5, 'OUTROS')) 
	tipo = models.IntegerField(choices=TIPOS_OCORRENCIAS)
	data_ocorrencia = models.DateField(null=True, blank=True)
	data_registro = models.DateField(auto_now=True)
	funcionario = models.ForeignKey(Funcionario, models.SET_NULL, blank=True, null=True,)
