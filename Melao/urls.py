from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Importa settings
from django.conf.urls.static import static # Importa static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('melaoapp.urls')),
    path('i18n/', include('django.conf.urls.i18n'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
