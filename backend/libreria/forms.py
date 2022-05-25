from    django  import  forms
from    .models import  servicio,   producto

class   servicioForm(forms.ModelForm):
    class   Meta:
        model   =   servicio
        fields  =   '__all__'

class   productoForm(forms.ModelForm):
    class Meta:
        model   =   producto
        fields  =   '__all__'