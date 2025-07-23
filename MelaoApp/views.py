from django.shortcuts import render
from django.http import HttpResponse

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

# melaoapp/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

def set_theme(request):
    """
    Vista para establecer la preferencia del tema (claro/oscuro) en una cookie.
    """
    if request.method == 'GET': # Podrías usar POST también, pero GET es más simple para un enlace/botón
        theme = request.GET.get('theme', 'light') # Obtiene 'theme' del parámetro URL, por defecto 'light'
        
        # Opcional: Asegurarse de que el tema sea válido
        if theme not in ['light', 'dark']:
            theme = 'light'

        # Redirigir a la página anterior o a una URL específica
        # request.META.get('HTTP_REFERER') contiene la URL de donde vino la solicitud
        response = redirect(request.META.get('HTTP_REFERER', '/')) 
        
        # Establecer la cookie 'theme'
        response.set_cookie('theme', theme, max_age=60*60*24*365) # La cookie durará un año

        return response
    # Si la solicitud no es GET, simplemente redirige o maneja el error
    return redirect('/') # O a donde sea apropiado