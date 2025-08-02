from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db import models

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

class Student(AbstractUser):
    """
    Modelo personalizado para representar a un estudiante en la aplicación.
    Extiende AbstractUser para aprovechar el sistema de autenticación de Django.
    """
    full_name = models.CharField(max_length=255)
    profile_picture_url = models.URLField(max_length=500, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    self_description = models.TextField(blank=True, null=True)
    favorite_color = models.CharField(max_length=50, blank=True, null=True)
    favorite_book = models.CharField(max_length=255, blank=True, null=True)
    favorite_music = models.CharField(max_length=255, blank=True, null=True)
    favorite_videogame = models.CharField(max_length=255, blank=True, null=True)
    known_programming_languages = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='student_set', 
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='student_permissions_set', 
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

class IsFriendOf(models.Model):
    username_1 = models.ForeignKey(Student, related_name='friends_as_user1', on_delete=models.CASCADE)
    username_2 = models.ForeignKey(Student, related_name='friends_as_user2', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('username_1', 'username_2'),)
        verbose_name_plural = "Friends Relationships"

    def __str__(self):
        return f"{self.username_1.username} is friend of {self.username_2.username}"

class Notification(models.Model):
    sending_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    type = models.CharField(max_length=50)
    username = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notification for {self.username.username} on {self.sending_date.strftime('%Y-%m-%d %H:%M')}"

class Chat(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat {self.id} created at {self.creation_time.strftime('%Y-%m-%d %H:%M')}"

class Has(models.Model):
    username = models.ForeignKey(Student, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('username', 'chat'),)
        verbose_name_plural = "Has Chat"

    def __str__(self):
        return f"{self.username.username} has chat {self.chat.id}"

class Message(models.Model):
    multimedia_url = models.URLField(max_length=500, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    sending_date = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender_username = models.ForeignKey(Student, related_name='sent_messages', on_delete=models.CASCADE)
    receiver_username = models.ForeignKey(Student, related_name='received_messages', on_delete=models.CASCADE)

    def __str__(self):
        return f"Message from {self.sender_username.username} to {self.receiver_username.username} in Chat {self.chat.id}"

class FriendRequest(models.Model):
    sender = models.ForeignKey(Student, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Student, related_name='received_requests', on_delete=models.CASCADE)
    type = models.CharField(max_length=50) # Por ejemplo: 'pending', 'accepted', 'rejected'
    request_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('sender', 'receiver'),)
        verbose_name_plural = "Friend Requests"
