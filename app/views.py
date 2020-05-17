from django.shortcuts import render
from django.http import HttpResponse
from app.models import Area, Vaga

# Create your views here.
def index(request):
    area = Area()
    area.capacidade = 3
    area.save()

    area.gerar_vagas()
    print(area.capacidade)
    

    return HttpResponse("OK")

