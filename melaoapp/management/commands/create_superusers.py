from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from melaoapp.models import Usuario

class Command(BaseCommand):
    help = 'Crea superusuarios y los asigna a grupos de administración'
    
    def handle(self, *args, **kwargs):
        # Crear grupos si no existen
        admin_group, created = Group.objects.get_or_create(name='Administradores')
        editores_group, created = Group.objects.get_or_create(name='Editores')
        
        # Asignar permisos a administradores
        admin_perms = Permission.objects.all()
        admin_group.permissions.set(admin_perms)
        
        # Permisos para editores
        editor_perms = Permission.objects.filter(
            codename__in=['add_post', 'change_post', 'view_post', 'publish_content', 'edit_content']
        )
        editores_group.permissions.set(editor_perms)
        
        # Crear superusuario admin
        admin_data = {
            'username': 'admin',
            'email': 'admin@example.com',
            'password': 'AdminPassword123',
            'is_staff': True,
            'is_superuser': True,
            'rol': 'ADMIN'
        }
        
        user, created = Usuario.objects.get_or_create(
            username=admin_data['username'],
            defaults=admin_data
        )
        
        if created or not user.check_password(admin_data['password']):
            user.set_password(admin_data['password'])
            user.save()
        
        # Asignar al grupo de Administradores
        admin_group.usuario_groups.add(user)
        
        self.stdout.write(self.style.SUCCESS(
            f'Usuario admin creado y asignado al grupo Administradores'
        ))
        
        # Crear usuario editor
        editor_data = {
            'username': 'editor',
            'email': 'editor@example.com',
            'password': 'EditorPassword123',
            'is_staff': True,
            'rol': 'EDITOR'
        }
        
        editor_user, created = Usuario.objects.get_or_create(
            username=editor_data['username'],
            defaults=editor_data
        )
        
        if created or not editor_user.check_password(editor_data['password']):
            editor_user.set_password(editor_data['password'])
            editor_user.save()
        
        # Asignar al grupo de Editores
        editores_group.usuario_groups.add(editor_user)
        
        self.stdout.write(self.style.SUCCESS('Usuario editor creado y asignado'))