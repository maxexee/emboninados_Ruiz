from    django.shortcuts    import  render, redirect
from    django.http         import  HttpResponse
from    .models             import  servicio
from    .forms              import  servicioForm

def inicio(request):
    return  render(request, 'paginas/inicio.html')

def nosotros(request):
    return  render(request, 'paginas/nosotros.html')

def servicios(request):
    s    =   servicio.objects.all()
    return  render(request, 'servicios/index.html', {'ser':  s})

def crearS(request):
    formulario  =   servicioForm(request.POST   or  None,   request.FILES    or  None)
    if  formulario.is_valid():
        formulario.save()
        return  redirect('servicios')
    return  render(request, 'servicios/crear.html', {'formulario':    formulario})

def editarS(request,    id):
    ser         =   servicio.objects.get(id=id)
    formulario  =   servicioForm(request.POST   or  None,   request.FILES   or  None,   instance=ser)
    if  formulario.is_valid()   and request.POST:
        formulario.save()
        return  redirect('servicios')
    return  render(request, 'servicios/editar.html',    {'formulario':  formulario})

def borrarS(request,    id):
    libro   =   servicio.objects.get(id=id)
    libro.delete()
    return  redirect('servicios')