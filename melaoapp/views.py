from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Is_friend_of, Post, Student, Notification
from django.http import JsonResponse
from django.utils import timezone
from datetime import date

def sign_up_view(request):
    return render(request, 'melaoapp/signUpView.html', {'form': form})

def chat_list_view(request):
    return render(request, 'melaoapp/chatListView.html')

def friends_list(request):
    current_student = Student.objects.get(user=request.user)

    friendships = Is_friend_of.objects.filter(
        Q(username_1=current_student) | Q(username_2=current_student)
    )

    friends_list = []
    for friendship in friendships:
        if friendship.username_1 == current_student:
            friends_list.append(friendship.username_2)
        else:
            friends_list.append(friendship.username_1)

    context = {'friends': friends_list}
    return render(request, 'melaoapp/friendsList.html', context)

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

def add_friend_notification(request):
    if request.method == 'POST':
        recipient_username = request.POST.get('recipient_username')

        sending_date = timezone.now()
        
        content = f"{request.user.username} te ha enviado una solicitud de amistad."
        
        notification_type = 'friend_request' 

        try:
            recipient_student = Student.objects.get(user__username=recipient_username)
            
            notification = Notification(
                sending_date=sending_date,
                content=content,
                type=notification_type,
                username=recipient_student)
            
            notification.save()
            
            return JsonResponse({'status': 'success', 'message': 'Solicitud de amistad enviada.'})
        
        except Student.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'El usuario destinatario no existe.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def view_notifications(request):
    try:
        current_student = request.user.student
    except Student.DoesNotExist:
        return render(request, 'error.html', {'message': 'No se encontró el perfil de estudiante.'})
    
    notifications = Notification.objects.select_related('sender_username').filter(receiver_username=current_student).order_by('-sending_date')

    context = {
        'notifications': notifications
    }

    return render(request, 'melaoapp/viewNotifications.html', context)

def home(request):
    try:
        current_student = Student.objects.get(user=request.user)
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

    posts = Post.objects.filter(
        username_id__in=friend_ids
    ).select_related(
        'username__user'
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

def new_post_view(request):
    if request.method == 'POST':
        # Crear una copia mutable de request.POST
        post_data = request.POST.copy()
        
        # Establecer un valor predeterminado para privacy_settings si no se proporciona
        if 'privacy_settings' not in post_data or not post_data['privacy_settings']:
            post_data['privacy_settings'] = '1'  # Valor predeterminado (público)
        
        form = PostForm(post_data, request.FILES)
        
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.username = request.user.student
            new_post.post_date = date.today()
            new_post.save()
            return redirect('melaoapp:home')
    else:
        # Crear formulario con valor predeterminado para escritorio
        form = PostForm(initial={'privacy_settings': 1})
    
    return render(request, 'melaoapp/newPostView.html', {'form': form})