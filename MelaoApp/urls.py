# ~/Universidad/ATI/Proyecto/Melao/MelaoApp/urls.py
from django.urls import path
from . import views

app_name = 'MelaoApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('productos/<int:id_producto>/', views.ver_producto, name='ver_producto'),
    path('lista/', views.lista_productos, name='lista_productos'),
]