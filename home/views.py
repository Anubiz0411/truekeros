from django.shortcuts import render
from django.template import RequestContext

# Create your views here.


def index_view(request):
	return render(request, 'home/index.html')
