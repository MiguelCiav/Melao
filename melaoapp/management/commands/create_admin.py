from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from melaoapp.models import Student  # Asegúrate de que apunte a tus modelos v2

class Command(BaseCommand):
    help = 'Crea un nuevo superusuario (administrador) con un perfil de estudiante asociado.'

    def add_arguments(self, parser):
        """Añade los argumentos que el comando recibirá desde la terminal."""
        parser.add_argument('username', type=str, help='El nombre de usuario para el nuevo administrador.')
        parser.add_argument('email', type=str, help='El correo electrónico del nuevo administrador.')
        parser.add_argument('password', type=str, help='La contraseña para el nuevo administrador.')
        parser.add_argument('--first_name', type=str, default='', help='(Opcional) El nombre del administrador.')
        parser.add_argument('--last_name', type=str, default='', help='(Opcional) El apellido del administrador.')

    def handle(self, *args, **options):
        """La lógica principal del comando."""
        username = options['username']
        email = options['email']
        password = options['password']
        
        if User.objects.filter(username=username).exists():
            raise CommandError(f'El usuario "{username}" ya existe. Por favor, elige otro nombre de usuario.')

        if User.objects.filter(email=email).exists():
            raise CommandError(f'El email "{email}" ya está en uso. Por favor, elige otro email.')

        self.stdout.write(self.style.NOTICE(f'Creando administrador: {username}...'))

        try:
            user = User.objects.create_superuser(username=username, email=email, password=password)
            user.first_name = options['first_name']
            user.last_name = options['last_name']
            user.save()
        except Exception as e:
            raise CommandError(f'Ocurrió un error al crear el superusuario: {e}')

        Student.objects.create(user=user)

        self.stdout.write(self.style.SUCCESS(
            f'✅ Administrador "{username}" y su perfil de estudiante han sido creados exitosamente.'
        ))