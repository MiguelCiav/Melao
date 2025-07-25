from django.db import models
from django.contrib.auth.models import AbstractUser

# MelaoApp/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

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