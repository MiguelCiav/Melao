# melaoapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Post
from django.db import transaction

class CustomUserCreationForm(UserCreationForm):
    # Campos adicionales para el registro
    email = forms.EmailField(required=True, help_text='Requerido.')
    first_name = forms.CharField(max_length=150, required=True, label="Nombre")
    last_name = forms.CharField(max_length=150, required=True, label="Apellido")
    date_of_birth = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Fecha de Nacimiento"
    )
    gender = forms.ChoiceField(
        choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')],
        required=False,
        label="Género"
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # Se especifican solo los campos que pertenecen al modelo User y los que maneja el formulario base.
        # Los campos extra (date_of_birth, gender) se manejan en el método save.
        fields = ("username", "email", "first_name", "last_name")

    @transaction.atomic
    def save(self, commit=True):
        # El método save ahora se encarga de crear el User y el Student de forma segura.
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        
        if commit:
            user.save()
            # Se crea el objeto Student asociado al usuario recién creado
            Student.objects.create(
                user=user,
                date_of_birth=self.cleaned_data['date_of_birth'],
                gender=self.cleaned_data.get('gender'),
            )
        return user

class StudentSelfDescriptionForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['self_description']

class PrivacySettingsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['private_profile']
        
class NotificationsSettingsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email_notifications']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['profile_picture']

class PostForm(forms.ModelForm):
    privacy_settings = forms.IntegerField(
        widget=forms.HiddenInput(),
        initial=1
    )
    class Meta:
        model = Post
        fields = ['description', 'multimedia', 'privacy_settings']
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Escribe lo que estás pensando...',
                'class': 'text-area-custom',
                'rows': 4
            }),
            'multimedia': forms.FileInput(attrs={
                'class': 'visually-hidden',
                'accept': 'image/*,video/*'
            }),
        }
