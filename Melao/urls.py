from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Importa settings
from django.conf.urls.static import static # Importa static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('melaoapp/', include('MelaoApp.urls')),
    path('', include('MelaoApp.urls')), # Redirige la raíz a las URLs de MelaoApp
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)