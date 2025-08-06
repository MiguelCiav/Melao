from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture_url = models.URLField(max_length=500, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    self_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Student, on_delete=models.CASCADE)
    description = models.TextField()
    multimedia_url = models.URLField(max_length=500, blank=True, null=True)
    privacy_settings = models.IntegerField()
    post_date = models.DateField(blank=True, null = True)

class Is_friend_of(models.Model):
    username_1 = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="friendships_initiated"
    )
    username_2 = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="friendships_received"
    )

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    sending_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    type = models.CharField(max_length=50)
    username = models.ForeignKey(Student, on_delete=models.CASCADE)

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    creation_time = models.DateField(blank =True, null=True)

class Has(models.Model):
    username = models.ForeignKey(Student, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    creation_time = models.DateField(blank=True, null=True)

class Sends_Request(models.Model):
    username_1 = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="sends_requests_sent"
    )
    username_2 = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="sends_requests_received"
    )
    type = models.TextField()

class Likes(models.Model):
    username = models.ForeignKey(Student, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_of_like = models.DateField(blank=True, null=True)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(Student, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(blank=True, null = True)

class Belongs_to(models.Model):
    parent_comment_id = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="parent_belongs"
    )
    child_comment_id = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="child_belongs"
    )