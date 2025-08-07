from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_views

app_name = 'melaoapp'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('chats/', views.chat_list_view, name='chat_list_view'),
    path('chat/', views.chat_view, name='chat_view'),
    path('friends/', views.friends_list, name='friends_list'),
    path('config/language-theme/', views.language_and_theme_config_view, name='language_and_theme_config_view'),
    path('profile/edit/', views.modify_profile, name='modify_profile'),
    path('new-post/', views.new_post_view, name='new_post_view'),
    path('post/', views.post_view, name='post_view'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search_person_view, name='search_person_view'),
    path('signup/', views.sign_up_view, name='sign_up_view'),
    path('notifications/', views.view_notifications, name='view_notifications'),
    path('', views.welcome, name='welcome'),
    path('welcome/', views.welcome, name='welcome-root'),
    path('set-theme/', views.set_theme, name='set_theme'),

    path('reset_password/',
        auth_views.PasswordResetView.as_view(
            template_name="melaoapp/password_reset.html",
            # url para el email, por defecto es password_reset_confirm
            email_template_name='melaoapp/password_reset_email.html', 
            success_url='/reset_password_sent/' 
            ),
        name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="melaoapp/password_reset_sent.html"),
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="melaoapp/password_reset_confirm.html",
            success_url='/reset_password_complete/'
            ),
        name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="melaoapp/password_reset_complete.html"),
         name="password_reset_complete"),
]
