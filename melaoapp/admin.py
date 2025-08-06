from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import (
    Student,
    Post,
    Is_friend_of,
    Notification,
    Chat,
    Has,
    Message,
    Sends_Request,
    Likes,
    Comment,
    Belongs_to
)

class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Perfil del Estudiante'
    fields = ('profile_picture_url', 'date_of_birth', 'gender', 'self_description')

class CustomUserAdmin(UserAdmin):
    inlines = (StudentInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('username', 'description', 'post_date', 'privacy_settings')
    list_filter = ('post_date', 'privacy_settings', 'username')
    search_fields = ('description', 'username__user__username')
    ordering = ('-post_date',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'post_id', 'text', 'date')
    search_fields = ('text', 'username__user__username', 'post_id__description')
    ordering = ('-date',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Is_friend_of)
admin.site.register(Notification)
admin.site.register(Chat)
admin.site.register(Has)
admin.site.register(Message)
admin.site.register(Sends_Request)
admin.site.register(Likes)
admin.site.register(Belongs_to)