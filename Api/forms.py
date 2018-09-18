from django import forms
from .models import Empresa
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            ] 
        labels = {
            'username': 'Usuario',
            'first_name': 'nombres',
            'last_name' : 'apellidos',
        }

class RegEmpForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = ['nombre', 'nit', 
        'id_tipo', 
        'direccion', 
        'logo',
        'id_tipo',
        'id_ciudad',
        'telefono',
        'celular',
        'email',
        'lema',
        'mision',
        'vision',
        'nombre_ser_1','ser_1',
            # 'nombre_ser_2', 'ser_2',
            # 'nombre_ser_3', 'ser_3',
            # 'nombre_ser_4', 'ser_4',
            # 'nombre_ser_5', 'ser_5',
        'fecha_registro'
        ]