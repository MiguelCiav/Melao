from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Post, AccessLog
from .forms import UsuarioEditForm, CustomUserCreationForm

class UsuarioAdmin(UserAdmin):  # Cambia a UserAdmin en lugar de ModelAdmin
    add_form = CustomUserCreationForm  # Formulario para añadir usuarios
    form = UsuarioEditForm  # Formulario para editar usuarios
    model = Usuario
    
    list_display = ('username', 'email', 'rol', 'is_staff', 'last_login')
    list_filter = ('rol', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Datos adicionales', {'fields': ('rol', 'date_of_birth', 'preferences', 'self_description')}),
        ('Registros', {'fields': ('last_login', 'date_joined', 'last_activity')}),
    )
    
    # AÑADE ESTE BLOQUE NUEVO
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'rol'),
        }),
    )

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'action', 'ip_address')
    list_filter = ('user', 'action')
    search_fields = ('user__username', 'action', 'ip_address')
    readonly_fields = ('timestamp',)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Post)