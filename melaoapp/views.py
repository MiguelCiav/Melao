from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Is_friend_of, Post, Student

def sign_up_view(request):
    return render(request, 'melaoapp/signUpView.html', {'form': form})

def chat_list_view(request):
    return render(request, 'melaoapp/chatListView.html')

def friends_list(request):
    return render(request, 'melaoapp/friendsList.html')

def language_and_theme_config_view(request):
    return render(request, 'melaoapp/languageAndThemeConfigView.html')

def modify_profile(request):
    return render(request, 'melaoapp/modifyProfile.html')

def new_post_view(request):
    return render(request, 'melaoapp/newPostView.html')

@login_required(login_url='melaoapp:welcome')
def profile(request):
    full_name = request.user.get_full_name()
    context = {"full_name": full_name}
    return render(request, 'melaoapp/profile.html', context)

def search_person_view(request):
    persons = Student.objects.select_related('user').all()
    context = {'persons': persons}
    return render(request, 'melaoapp/searchPersonView.html', context)

def view_notifications(request):
    return render(request, 'melaoapp/viewNotifications.html')

def home(request):
    current_user = request.user.username

    friends_of_user = Is_friend_of.objects.filter(username_1=current_user).values_list('username_2', flat=True)

    posts = Post.objects.filter(
        username__in=friends_of_user
    ).select_related(
        'student'
    ).order_by(
        '-post_date'
    )[:100]

    return render(request, 'melaoapp/home.html', {'posts': posts})

def chat_view(request):
    return render(request, 'melaoapp/chatView.html')

def language_and_theme_config_view(request):
    return render(request, 'melaoapp/languageAndThemeConfigView.html')

def post_view(request):
    return render(request, 'melaoapp/postView.html')

def sign_up_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('melaoapp:welcome')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'melaoapp/signUpView.html', {'form': form})

def welcome(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('melaoapp:home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'melaoapp/welcome.html', {'form': form})

def set_theme(request):
    if request.method == 'GET':
        theme = request.GET.get('theme', 'light')
        if theme not in ['light', 'dark']:
            theme = 'light'
        response = redirect(request.META.get('HTTP_REFERER', '/')) 
        response.set_cookie('theme', theme, max_age=60*60*24*365)
        return response
    return redirect('/')