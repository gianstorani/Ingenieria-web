from django.shortcuts import render
from .forms import PublicacionForm
from django.contrib.auth.decorators import login_required	

# Create your views here.

@login_required
def nuevapublicacion(request):
	if request.method == 'POST':
		form = PublicacionForm(request.POST)
	else:
		form = PublicacionForm(request.POST)
	return render(request, 'nuevapublicacion.html',{ 'form': form })