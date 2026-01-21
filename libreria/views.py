from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("Hello, world!")

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    return render(request, 'libros/index.html')

def crear_libro(request):
    return render(request, 'libros/crear.html') 

def editar_libro(request):
    return render(request, 'libros/editar.html')

def eliminar_libro(request):
    return render(request, 'libros/eliminar.html') 

def detalle_libro(request):
    return render(request, 'libros/detalle.html') 