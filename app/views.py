from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import *
from app.controllers import *

# Create your views here.
def index(request):
	dados = {'titulo':'Home Page', 'areas':[]}
	lista_de_areas = AreaController.listar_areas()
	
	for area in lista_de_areas:
		n_vagas = VagaController.contar_vagas_livres(area)
		dados['areas'].append([area, n_vagas])
		print(dados['areas'])
	dados['areas'] = lista_de_areas
	return render(request, 'home-page.html', dados)

def nova_area(request):
	return render(request, 'area/formulario.html')

def salvar_area(request):
	if request.POST:
		area = {'nome': request.POST['nome'], 'capacidade': request.POST['capacidade']}
		AreaController.salvar_area(area)
		return redirect('home')

