# urls.py
from django.urls import path, re_path
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('nova/area/', views.nova_area, name='formulario_area'),
    path('salvar/area/', views.salvar_area, name='salvar_area'),
    ]
