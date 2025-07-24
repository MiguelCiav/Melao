from django.urls import path
from . import views

app_name = 'MelaoApp'

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
    path('sign_up_save/', views.sign_up_save, name='sign_up_save'),
]