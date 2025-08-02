# MelaoApp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario, Group
from django.contrib.auth.models import Permission

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol', 'password1', 'password2']
        labels = {
            'rol': 'Rol de usuario'
        }
        
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol', 'password1', 'password2']

class UsuarioEditForm(UserChangeForm):
    password = None  # No mostrar el campo de contraseña aquí
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol', 'first_name', 'last_name', 
                 'date_of_birth', 'preferences', 'self_description', 
                 'is_active', 'groups', 'user_permissions']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar la visualización de grupos y permisos
        self.fields['groups'].widget = forms.CheckboxSelectMultiple()
        self.fields['groups'].queryset = Group.objects.all()
        
        self.fields['user_permissions'].widget = forms.CheckboxSelectMultiple()
        self.fields['user_permissions'].queryset = Permission.objects.filter(
            content_type__app_label='MelaoApp'
        )