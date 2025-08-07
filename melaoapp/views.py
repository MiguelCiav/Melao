from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, PostForm, PrivacySettingsForm, NotificationsSettingsForm, StudentSelfDescriptionForm, ProfilePictureForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Is_friend_of, Post, Student, Notification
from .forms import StudentSelfDescriptionForm
from django.http import JsonResponse
from django.utils import timezone
import json
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from datetime import date


def sign_up_view(request):
    return render(request, 'melaoapp/signUpView.html', {'form': form})

@login_required(login_url='melaoapp:welcome')
def chat_list_view(request):
    return render(request, 'melaoapp/chatListView.html')

@login_required(login_url='melaoapp:welcome')
def friends_list(request):
    current_student = Student.objects.get(user=request.user)
    
    friendships = Is_friend_of.objects.filter(Q(username_1=current_student))
    
    friends = []
    for friendship in friendships:
        if friendship.username_1 == current_student:
            friends.append(friendship.username_2)
            
    context = {'friends': friends}
    return render(request, 'melaoapp/friendsList.html', context)

@login_required(login_url='melaoapp:welcome')
def language_and_theme_config_view(request):
    return render(request, 'melaoapp/languageAndThemeConfigView.html')

@login_required(login_url='melaoapp:welcome')
def modify_profile(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfilePictureForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('melaoapp:modify_profile')
    else:
        form = ProfilePictureForm(instance=student)
    return render(request, 'melaoapp/modifyProfile.html', {'form': form})

@login_required(login_url='melaoapp:welcome')
def new_post_view(request):
    return render(request, 'melaoapp/newPostView.html')

@login_required(login_url='melaoapp:welcome')
def profile(request):
    full_name = request.user.get_full_name()
    self_description = request.user.student.self_description
    context = {"full_name": full_name, "self_description": self_description}
    return render(request, 'melaoapp/profile.html', context)

@login_required(login_url='melaoapp:welcome')
def search_person_view(request):
    persons = Student.objects.select_related('user').exclude(user=request.user)
    context = {'persons': persons}
    return render(request, 'melaoapp/searchPersonView.html', context)

  
@login_required(login_url='melaoapp:welcome')
def send_notification(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            recipient_username = body_data.get('recipient_username')
            sender_username = body_data.get('sender_username')
            notification_type = body_data.get('type')

            if not recipient_username or not sender_username or not notification_type:
                return JsonResponse({'status': 'error', 'message': 'Datos incompletos.'}, status=400)

            sender_student = Student.objects.get(user__username=sender_username)
            recipient_student = Student.objects.get(user__username=recipient_username)

            notification = Notification(
                sender_username=sender_student,
                sending_date=timezone.now(),
                type=notification_type,
                receiver_username=recipient_student
            )

            notification.save()
            
            return JsonResponse({'status': 'success'})

        except Student.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'El remitente o destinatario no existe.'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Formato JSON inválido.'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Ocurrió un error inesperado: {str(e)}'}, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)

@login_required(login_url='melaoapp:welcome')
def accept_friend_request(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        
        sender_username_str = body_data.get('sender')

        if not sender_username_str:
            return JsonResponse({'status': 'error', 'message': 'Datos de usuario incompletos.'}, status=400)
        
        current_student = Student.objects.get(user=request.user)
        
        try:
            sender_student = Student.objects.get(user__username=sender_username_str)
        except Student.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'El usuario que envía la solicitud no existe.'}, status=404)

        Is_friend_of.objects.create(
            username_1=sender_student,
            username_2=current_student
        )
        
        Is_friend_of.objects.create(
            username_1=current_student,
            username_2=sender_student
        )

        return JsonResponse({'status': 'success', 'message': 'Amistad aceptada con éxito.'})

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Formato JSON inválido.'}, status=400)
    
    except Student.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El usuario actual no existe como estudiante.'}, status=404)
    
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': f'Ha ocurrido un error: {str(e)}'}, status=500)

@login_required(login_url='melaoapp:welcome')
def view_notifications(request):
    current_student = Student.objects.get(user=request.user)

    notifications = Notification.objects.filter(receiver_username=current_student)

    context = {
        'notifications': notifications
    }

    return render(request, 'melaoapp/viewNotifications.html', context)

@login_required(login_url='melaoapp:welcome')
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

@login_required(login_url='melaoapp:welcome')
def chat_view(request):
    return render(request, 'melaoapp/chatView.html')

@login_required(login_url='melaoapp:welcome')
def language_and_theme_config_view(request):
    return render(request, 'melaoapp/languageAndThemeConfigView.html')

@login_required(login_url='melaoapp:welcome')
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

@login_required
def about_me_config_view(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        form = StudentSelfDescriptionForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('melaoapp:profile')
    else:
        form = StudentSelfDescriptionForm(instance=student)
    return render(request, 'melaoapp/aboutMeConfigView.html', {'form': form})

@login_required(login_url='melaoapp:welcome')
def privacy_config_view(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        form = StudentSelfDescriptionForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('melaoapp:profile')
    else:
        form = StudentSelfDescriptionForm(instance=student)
    return render(request, 'melaoapp/aboutMeConfigView.html', {'form': form})

@login_required(login_url='melaoapp:welcome')
def notifications_config_view(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        form = StudentSelfDescriptionForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('melaoapp:profile')
    else:
        form = StudentSelfDescriptionForm(instance=student)
    return render(request, 'melaoapp/aboutMeConfigView.html', {'form': form})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'melaoapp/passwordChangeView.html'
    success_url = reverse_lazy('melaoapp:modify_profile')

@login_required
def privacy_config_view(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        form = PrivacySettingsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('melaoapp:privacy_config')
    else:
        form = PrivacySettingsForm(instance=student)
    return render(request, 'melaoapp/privacyConfigView.html', {'form': form})

@login_required
def notifications_config_view(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        form = NotificationsSettingsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('melaoapp:notifications_config')
    else:
        form = NotificationsSettingsForm(instance=student)
    return render(request, 'melaoapp/notificationsConfigView.html', {'form': form})

@login_required(login_url='melaoapp:welcome')
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
