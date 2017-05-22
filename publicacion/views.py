from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, PermissionDenied 
from .models import Entrada
from .forms import PostForm
# Create your views here.

class IndexView(ListView):
	"""docstring for IndexView"""
	template_name = 'publicacion.html'
	model = Entrada	

class EntradaDetailView(DetailView):
	"""docstring for EntradaDetailView"""
	template_name = 'entrada_detail.html'
	model = Entrada

class CrearPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Esta clase crea un nuevo post.
    """
    model = Entrada
    form_class = PostForm
    template_name = 'crear_post.html'
    login_url = reverse_lazy('account_login')
    success_message = u'El post %(titulo)s ha sido creado exitosamente.'


class EditarPost(SuccessMessageMixin, UpdateView):

    model = Entrada
    form_class = PostForm
    template_name = 'editar_post.html'

    success_message = u'El post %(titulo)s ha sido editado.'


class EliminarPost(DeleteView):
    model = Entrada
    context_object_name = 'post'
    template_name = 'eliminar.html'


