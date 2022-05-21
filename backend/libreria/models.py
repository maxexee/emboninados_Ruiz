from django.db import models

class   servicio(models.Model):
    id  =   models.AutoField(primary_key=True)
    titulo  =   models.AutoField(max_length=100,    verbose_name='Titulo')
    descripcion =   models.TextField(verbose_name='Descripción',    null=True)
