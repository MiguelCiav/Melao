# melaoapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario, Group, Student
from django.contrib.auth.models import Permission

class StudentRegistrationForm(UserCreationForm):
    # Añade los campos específicos de Student aquí si son requeridos
    full_name = forms.CharField(max_length=255, required=True, label="Nombre completo")
    date_of_birth = forms.DateField(required=True, label="Fecha de nacimiento", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta(UserCreationForm.Meta):
        model = Student
        # Añade los campos específicos de tu modelo Student
        fields = UserCreationForm.Meta.fields + ('full_name', 'email', 'date_of_birth',)
        # Personaliza los labels
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
        }


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
            content_type__app_label='melaoapp'
        )