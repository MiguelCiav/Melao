from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(
        choices=[
            ('M', 'Masculino'),
            ('F', 'Femenino'),
            ('O', 'Otro'),
        ],
        required=False
    )
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = ["username", 
                  "email", 
                  "first_name", 
                  "last_name", 
                  "date_of_birth", 
                  "gender", 
                  "password1", 
                  "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            Student.objects.create(
                user=user,
                date_of_birth=self.cleaned_data['date_of_birth'],
                gender=self.cleaned_data.get('gender', None),
            )
        return user

class StudentSelfDescriptionForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['self_description']

class StudentPrivacyForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['private_profile']

class StudentNotificationsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['email_notifications']