from distutils.command.upload import upload
from pickle import TRUE
from    django.db   import  models
from requests import delete

class   servicio(models.Model):
    id          =   models.AutoField(primary_key=True)
    titulo      =   models.CharField(max_length=100,    verbose_name='Titulo')
    descripcion =   models.TextField(verbose_name='Descripción',   null=True)

    def __str__(self):
        # fila    =   f'Título:   {self.titulo}   --  Descripción:    {self.descripcion}'
        return  f'Título:   {self.titulo}   --  Descripción:    {self.descripcion}'

    def delete(self, using=None):
        super().delete()


class   producto(models.Model):
    id          =   models.AutoField(primary_key=True)
    nombre      =   models.CharField(max_length=100,    verbose_name='Nombre')
    descripcion =   models.TextField(verbose_name='Descripción',   null=True)
    imagen      =   models.ImageField(upload_to =   'imagenes/',  verbose_name='Imagen',  null    =   True)

    def __str__(self):
        return  f'Nombre:   {self.nombre}   --  Descripción:    {self.descripcion}'

    def delete(self,    using=None):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()