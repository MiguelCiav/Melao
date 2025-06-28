# ~/Universidad/ATI/Proyecto/Melao/Melao/urls.py

from django.contrib import admin
from django.urls import path, include # Asegúrate de que 'include' esté importado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('melaoapp/', include('MelaoApp.urls')), # Esto ya lo deberías tener.
    # Agrega esta línea para la ruta raíz
    path('', include('MelaoApp.urls')), # Redirige la raíz a las URLs de MelaoApp
]