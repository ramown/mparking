from app.models import *
from django.http import HttpResponse


# Create your views here.
class AreaController():
	def listar_areas():
		return Area.objects.all()

	def salvar_area(area_capturada):
		area = Area()
		area.nome = area_capturada['nome']
		area.capacidade = area_capturada['capacidade']
		area.save()
    
class VagaController():
	def listar_vagas():
		return Vaga.objects.all()

	def contar_vagas_livres(area):
		n_vagas = list(Vaga.objects.filter(area=area, ocupada=True))
		return len(n_vagas)
