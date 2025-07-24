from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Estudiante
from django.contrib import messages

def registrar_estudiante(request):
    if request.method == 'POST':

        # recuperar la data del POST para devolverla al formulario por si hay error, esto para que el usuario 
        # no tenga que volver a llenar todo el form
        form_data = {
            'full_name': request.POST.get('name', ''),
            'user': request.POST.get('user', ''),
            'email': request.POST.get('email', ''),
            'birth_date': request.POST.get('birth_date', ''),
        }

        email = request.POST['email']
        user = request.POST['user']
        
        #1- Validar que el user ya este registrado
        if Estudiante.objects.filter(user=user).exists():
            messages.error(request, '¡Este nombre de usuario ya está en uso!')
            return render(request, 'MelaoApp/signUpView.html', {'form_data': form_data})  # Vuelve al formulario

        #2- Validar que el email ya este registrado
        if Estudiante.objects.filter(email=email).exists():
            messages.error(request, '¡Este email ya está registrado!')
            return render(request, 'MelaoApp/signUpView.html', {'form_data': form_data})  # Vuelve al formulario
        
        try:
            estudiante = Estudiante(
                full_name = request.POST['name'],
                user = request.POST['user'],
                email = request.POST['email'],
                password = request.POST['password'],
                bith_date = request.POST['birth_date'],
            )

            estudiante.save()
            messages.success(request, '¡Estudiante registrado exitosamente!')
            return render(request, 'MelaoApp/welcome.html', ) #vuelve al welcome con el mensaje exitoso
        except Exception as e:
            messages.error(request,e)
            return render(request, 'MelaoApp/signUpView.html', {'form_data': form_data})  # Vuelve al formulario

    # Si es GET o hay errores, muestra el formulario
    return render(request, 'MelaoApp/signUpView.html')

def home(request):
    return render(request, 'MelaoApp/home.html')

def chat_list_view(request):
    return render(request, 'MelaoApp/chatListView.html')

def chat_view(request):
    return render(request, 'MelaoApp/chatView.html')

def friends_list(request):
    return render(request, 'MelaoApp/friendsList.html')

def language_and_theme_config_view(request):
    return render(request, 'MelaoApp/languageAndThemeConfigView.html')

def modify_profile(request):
    return render(request, 'MelaoApp/modifyProfile.html')

def new_post_view(request):
    return render(request, 'MelaoApp/newPostView.html')

def post_view(request):
    return render(request, 'MelaoApp/postView.html')

def profile(request):
    return render(request, 'MelaoApp/profile.html')

def search_person_view(request):
    return render(request, 'MelaoApp/searchPersonView.html')

def sign_up_view(request):
    return render(request, 'MelaoApp/signUpView.html')

def view_notifications(request):
    return render(request, 'MelaoApp/viewNotifications.html')

def welcome(request):
    return render(request, 'MelaoApp/welcome.html')