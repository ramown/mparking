from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Area(models.Model):
    nome = models.CharField(max_length=30)
    capacidade = models.IntegerField()
    ativo = models.BooleanField(default=True)

    def gerar_vagas(self):
    	for item in range(self.capacidade):
    		vaga = Vaga()
    		vaga.area = self
    		vaga.save()

    def __str__(self):
    	return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=50)
    data_inicio = models.DateField(null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)
    areas_usadas = models.ManyToManyField(Area)
    def __str__(self):
    	return self.nome

class Pessoa(models.Model):
	nome = models.CharField(max_length=50)


class Funcionario(Pessoa):
	matricula = models.CharField(max_length=15)
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
    	return self.nome

class Proprietario(Pessoa):
	TIPOS_PROPS = (
		(0, 'ALUNO'), 
		(1, 'PROFESSORES'), 
		(2, 'ADMINISTRATIVO'), 
		(3, 'VISITANTES'),) 
	tipo = models.IntegerField(choices=TIPOS_PROPS)
    def __str__(self):
    	return self.nome

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
	funcionario = models.ForeignKey(Funcionario, models.SET_NULL, blank=True, null=True)
	descricao = models.TextField()


class Veiculo(models.Model):
	CATEGORIAS_VEICULOS = (
		(0, 'PREFERENCIAL'),
		(1, 'FUNCIONARIO'), 
		(2, 'ALUNO'),
 		(6, 'VISITANTE'))
	CATEGORIAS_TIPO = (
		(0, 'CARRO'), 
		(1, 'MOTOCICLETA'), 
		(2, 'VAN'), 
		(3, 'ÔNIBUS'),
		)
	placa = models.CharField(max_length=15)
	modelo = models.CharField(max_length=20)
	marca = models.CharField(max_length=15)
	tipo = models.IntegerField(choices=CATEGORIAS_TIPO)
	categoria = models.IntegerField(choices=CATEGORIAS_VEICULOS)
	proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)
    def __str__(self):
    	return self.nome


class Vaga(models.Model):
	veiculo = models.ForeignKey(Veiculo, models.SET_NULL, blank=True, null=True)
	area = models.ForeignKey(Area, models.SET_NULL, blank=True, null=True)
	ocupada = models.BooleanField(default=False)
	
	def ocupar(self):
		self.ocupada = True
		self.save()

	def desocupar(self):
		self.ocupada = False
		self.save()

class LogDeEstacionamento(models.Model):
	veiculo = models.ForeignKey(Veiculo, models.SET_NULL, blank=True, null=True)
	area = models.ForeignKey(Area, models.SET_NULL, blank=True, null=True)
	data_entrada = models.DateField(null=True, blank=True)
	data_saida = models.DateField(null=True, blank=True)
	
	def entrando(self):
		self.data_entrada = timezone.now()
		self.save()

	def saindo(self):
		self.data_saida = timezone.now()
		self.save()	
