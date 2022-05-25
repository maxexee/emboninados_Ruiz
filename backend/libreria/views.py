from    django.shortcuts    import  render, redirect
from    django.http         import  HttpResponse
from    .models             import  servicio,   producto
from    .forms              import  servicioForm,   productoForm

#SERVICIOS...

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

#PRODUCTOS...

def productos(request):
    prod    =   producto.objects.all()
    return  render(request, 'productos/index_p.html',   {'productos'    :   prod})

def crearP(request):
    formulario  =   productoForm(request.POST or None,  request.FILES    or  None)
    if  formulario.is_valid():
        formulario.save()
        return  redirect('productos')
    return  render(request, 'productos/crear_p.html',   {'formulario':  formulario})

def editarP(request,    id):
    prod    =   producto.objects.get(id=id)
    formulario  =   productoForm(request.POST   or  None, request.FILES or  None,   instance=prod)
    if  formulario.is_valid()   and request.POST:
        formulario.save()
        return  redirect('productos')
    return  render(request, 'productos/editar_p.html',  {'formulario':  formulario})

def borrarP(request,    id):
    prod    =   producto.objects.get(id=id)
    prod.delete()
    return  redirect('productos')