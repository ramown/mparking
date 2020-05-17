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
    

