from    django.db   import  models

class   servicio(models.Model):
    id          =   models.AutoField(primary_key=True)
    titulo      =   models.CharField(max_length=100,    verbose_name='Titulo')
    descripcion =   models.TextField(verbose_name='Descripción',   null=True)

    def __str__(self):
        # fila    =   f'Título:   {self.titulo}   --  Descripción:    {self.descripcion}'
        return  f'Título:   {self.titulo}   --  Descripción:    {self.descripcion}'

    def delete(self, using=None):
        super().delete()
