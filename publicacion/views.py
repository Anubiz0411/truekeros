from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entrada
# Create your views here.

class IndexView(ListView):
	"""docstring for IndexView"""
	template_name = 'publicacion.html'
	model = Entrada	

class EntradaDetailView(DetailView):
	"""docstring for EntradaDetailView"""
	template_name = 'entrada_detail.html'
	model = Entrada



