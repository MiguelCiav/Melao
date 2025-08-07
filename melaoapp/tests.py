# melaoapp/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Student, Post, Is_friend_of, Notification
import datetime

# ==============================================================================
# PRUEBAS PARA LOS MODELOS (Models)
# ==============================================================================

class ModelCreationTests(TestCase):
    """
    Pruebas para asegurar la correcta creación de los modelos principales.
    """
    def setUp(self):
        # Crear un usuario base para asociarlo a los modelos
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

    def test_student_model_creation(self):
        """Prueba que un objeto Student se puede crear y se representa por su username."""
        student = Student.objects.create(user=self.user, date_of_birth='2000-01-01')
        self.assertEqual(str(student), self.user.username)
        self.assertEqual(Student.objects.count(), 1)

    def test_post_model_creation(self):
        """Prueba que un objeto Post se puede crear correctamente."""
        student = Student.objects.create(user=self.user)
        post = Post.objects.create(
            username=student,
            description="Esta es una descripción de prueba.",
            privacy_settings=1,
            post_date=datetime.date.today()
        )
        self.assertEqual(str(post.username), 'testuser')
        self.assertEqual(Post.objects.count(), 1)


# ==============================================================================
# PRUEBAS PARA LAS VISTAS (Views)
# ==============================================================================

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            first_name='Test',
            last_name='User'
        )
        self.student1 = Student.objects.create(
            user=self.user,
            date_of_birth=datetime.date(2000, 1, 1),
            gender='M'
        )
        
        self.user2 = User.objects.create_user(
            username='usuario2',
            password='password2',
            first_name='Maria',
            last_name='Gómez'
        )
        self.student2 = Student.objects.create(
            user=self.user2,
            date_of_birth=datetime.date(2001, 2, 2),
            gender='F'
        )

    def test_friends_list_view(self):
        """Prueba que la lista de amigos muestra los amigos correctos."""
        # Hacer amigos a student1 y student2
        Is_friend_of.objects.create(username_1=self.student1, username_2=self.student2)

        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('melaoapp:friends_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'melaoapp/friendsList.html')
        # Verifica que el amigo está en la lista del contexto
        self.assertIn(self.student2, response.context['friends'])