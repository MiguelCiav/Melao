from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Importa settings
from django.conf.urls.static import static # Importa static
from MelaoApp.views import AdminLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/logout/', AdminLogoutView.as_view(), name='admin_logout'),
    path('', include('melaoapp.urls')), # Redirige la raíz a las URLs de MelaoApp
    path('melaoapp/', include('melaoapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
