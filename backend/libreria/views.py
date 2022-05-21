from    django.shortcuts    import render
from    django.http         import  HttpResponse

def inicio(request):
    return  render(request, 'paginas/inicio.html')

def nosotros(request):
    return  render(request, 'paginas/nosotros.html')

def servicios(request):
    return  render(request, 'servicios/index.html')

def crearS(request):
    return  render(request, 'servicios/crear.html')

def editarS(request):
    return  render(request, 'servicios/editar.html')