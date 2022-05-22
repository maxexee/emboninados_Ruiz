from pyexpat import model
from    django  import  forms
from    .models import  servicio

class   servicioForm(forms.ModelForm):
    class   Meta:
        model   =   servicio
        fields  =   '__all__'