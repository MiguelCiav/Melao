from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(AbstractUser):
    ROLES = (
        ('ADMIN', 'Administrador'),
        ('EDITOR', 'Editor'),
        ('LECTOR', 'Lector'),
        ('INVITADO', 'Invitado'),
    )
    
    rol = models.CharField(max_length=20, choices=ROLES, default='LECTOR')
    date_of_birth = models.DateField(null=True, blank=True)
    preferences = models.TextField(blank=True)
    self_description = models.TextField(blank=True)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    last_activity = models.DateTimeField(null=True, blank=True)

    # Relación con grupos (roles)
    groups = models.ManyToManyField(
        Group,
        verbose_name='Grupos',
        blank=True,
        help_text='Los grupos a los que pertenece este usuario',
        related_name="usuario_groups",
        related_query_name="usuario",
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='Permisos de usuario',
        blank=True,
        help_text='Permisos específicos para este usuario',
        related_name="usuario_permissions",
        related_query_name="usuario",
    )

    def __str__(self):
        return self.username

    def has_role(self, role_name):
        return self.rol == role_name

    def assign_role(self, role_name):
        if role_name in dict(self.ROLES).keys():
            self.rol = role_name
            self.save()
            return True
        return False
    
    class Meta:
        permissions = [
            ("view_audit_logs", "Puede ver los registros de auditoría"),
            ("manage_users", "Puede administrar usuarios"),
            ("manage_roles", "Puede administrar roles y permisos"),
            ("publish_content", "Puede publicar contenido"),
            ("edit_content", "Puede editar contenido"),
        ]



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
    

class AccessLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.timestamp} - {self.user} - {self.action}"

# MelaoApp/models.py (continuación)

