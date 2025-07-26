# MelaoApp/middleware.py
import threading
from django.utils import timezone
from .models import AccessLog, Usuario

request_local = threading.local()

class AuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Guardar la solicitud para acceso en otros lugares
        request_local.request = request
        
        # Procesar la solicitud
        response = self.get_response(request)
        
        # Registrar actividad del usuario
        if request.user.is_authenticated:
            Usuario.objects.filter(pk=request.user.pk).update(
                last_activity=timezone.now()
            )
        
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            action = f"Acceso a: {view_func.__name__}"
            AccessLog.objects.create(
                user=request.user,
                action=action,
                ip_address=self.get_client_ip(request),
                details=f"URL: {request.path}"
            )
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


def get_current_request():
    return getattr(request_local, 'request', None)