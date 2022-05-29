from    django.urls import  path

from libreria.models import producto
from    .   import  views
from    django.conf import  settings
from    django.contrib.staticfiles.urls import  static

urlpatterns  =   [

    #SERVICIO...
    path('',views.nosotros,    name='nosotros'),
    path('nosotros',    views.nosotros, name='nosotros'),
    path('servicios',   views.servicios,    name='servicios'),
    path('servicios/crear',   views.crearS,   name='crear'),
    path('borrarS/<int:id>',    views.borrarS, name='borrar'),
    path('servicios/editarS/<int:id>',   views.editarS,  name='editar'),    

    #PRODUCTOS...
    path('productos',   views.productos,    name='productos'),
    path('productos/crear',    views.crearP,   name='crearP'),
    # path('productos/editar',    views.editarP,  name='editarP'),
    path('borrarP/<int:id>',    views.borrarP,  name='borrarP'),
    path('producto/editar/<int:id>', views.editarP,  name='editarP')

]+static(settings.MEDIA_URL,    document_root   =   settings.MEDIA_ROOT)