from    django.urls import  path
from    .   import  views

urlpatterns  =   [
    path('',views.inicio,    name='inicio'),
    path('nosotros',    views.nosotros, name='nosotros'),
    path('servicios',   views.servicios,    name='servicios'),
    path('servicios/crear',   views.crearS,   name='crear'),
    path('servicios/editar',    views.editarS,  name='editar'),
    path('borrarS/<int:id>',    views.borrarS, name='borrar'),
]