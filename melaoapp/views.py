# melaoapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Is_friend_of, Post, Student, Notification
from django.http import JsonResponse
from datetime import date

# Vista de Registro (versión única y corregida)
def sign_up_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # El método save del formulario ahora hace todo el trabajo.
            return redirect('melaoapp:welcome')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'melaoapp/signUpView.html', {'form': form})

# Vista de Login
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

# Vista de Inicio (Home)
@login_required(login_url='melaoapp:welcome')
def home(request):
    try:
        current_student = request.user.student
    except Student.DoesNotExist:
        return render(request, 'melaoapp/home.html', {'posts': []})

    friendships = Is_friend_of.objects.filter(
        Q(username_1=current_student) | Q(username_2=current_student)
    )

    friend_ids = []
    for friendship in friendships:
        if friendship.username_1 == current_student:
            friend_ids.append(friendship.username_2.id)
        else:
            friend_ids.append(friendship.username_1.id)

    posts = Post.objects.filter(username_id__in=friend_ids).select_related('username__user').order_by('-post_date')[:100]
    return render(request, 'melaoapp/home.html', {'posts': posts})

# Vista para crear un nuevo post
@login_required(login_url='melaoapp:welcome')
def new_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.username = request.user.student
            new_post.post_date = date.today()
            new_post.save()
            return redirect('melaoapp:home')
    else:
        form = PostForm()
    
    return render(request, 'melaoapp/newPostView.html', {'form': form})

# Vista del perfil de usuario
@login_required(login_url='melaoapp:welcome')
def profile(request):
    full_name = request.user.get_full_name()
    context = {"full_name": full_name}
    return render(request, 'melaoapp/profile.html', context)

# Vista para ver notificaciones (Corregido el acceso a 'student')
@login_required(login_url='melaoapp:welcome')
def view_notifications(request):
    try:
        current_student = request.user.student
        notifications = Notification.objects.select_related('sender_username__user').filter(receiver_username=current_student).order_by('-sending_date')
        context = {'notifications': notifications}
        return render(request, 'melaoapp/viewNotifications.html', context)
    except Student.DoesNotExist:
        return render(request, 'error.html', {'message': 'No se encontró el perfil de estudiante.'})

# Vista para enviar notificación de amistad (API) (Corregida)
@login_required
def add_friend_notification(request):
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient_username')
        try:
            sender_student = request.user.student
            recipient_student = Student.objects.get(user__username=recipient_username)
            
            content = f"{request.user.username} te ha enviado una solicitud de amistad."
            notification_type = 'friend_request' 

            Notification.objects.create(
                sender_username=sender_student,
                receiver_username=recipient_student,
                content=content,
                type=notification_type
            )
            return JsonResponse({'status': 'success', 'message': 'Solicitud de amistad enviada.'})
        except Student.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'El usuario no existe.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

# ----- Vistas restantes y utilidades -----

@login_required(login_url='melaoapp:welcome')
def friends_list(request):
    current_student = request.user.student
    friendships = Is_friend_of.objects.filter(Q(username_1=current_student) | Q(username_2=current_student))
    friends = [f.username_2 if f.username_1 == current_student else f.username_1 for f in friendships]
    return render(request, 'melaoapp/friendsList.html', {'friends': friends})

@login_required(login_url='melaoapp:welcome')
def search_person_view(request):
    persons = Student.objects.select_related('user').all()
    return render(request, 'melaoapp/searchPersonView.html', {'persons': persons})

def set_theme(request):
    if request.method == 'GET':
        theme = request.GET.get('theme', 'light')
        response = redirect(request.META.get('HTTP_REFERER', '/')) 
        response.set_cookie('theme', theme, max_age=31536000) # 1 año
        return response
    return redirect('/')

# Vistas de plantilla simples
def chat_list_view(request):
    return render(request, 'melaoapp/chatListView.html')

def chat_view(request):
    return render(request, 'melaoapp/chatView.html')

def language_and_theme_config_view(request):
    return render(request, 'melaoapp/languageAndThemeConfigView.html')

def modify_profile(request):
    return render(request, 'melaoapp/modifyProfile.html')
    
def post_view(request):
    return render(request, 'melaoapp/postView.html')