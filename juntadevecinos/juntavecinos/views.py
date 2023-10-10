from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Vecinos,Noticias,Propuesta,Proyectos,Actividades
from .forms import NoticiasForm, ActividadesForm, ProyectosForm, PropuestaForm, VecinosForm
# Create your views here.

def inicio(request):    
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def crear(request):
    formularionoticia = NoticiasForm(request.POST or None, request.FILES or None)
    if formularionoticia.is_valid():
        formularionoticia.save()
        return redirect('crear')
    return render(request, 'juntas/crear.html', {'formularionoticia':formularionoticia})


def index(request):
    noticias = Noticias.objects.all().order_by('id')
    print (Noticias)
    return render(request, 'juntas/index.html', {'noticias':noticias})


def form(request):
    return render(request, 'juntas/form.html')


def noticias(request):
    noticias = Noticias.objects.all().order_by('id')
    print (Noticias)
    return render(request, 'juntas/noticias.html', {'noticias':noticias})	