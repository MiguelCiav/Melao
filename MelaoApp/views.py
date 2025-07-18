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

def login_view(request):
    return render(request, 'MelaoApp/loginView.html')

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