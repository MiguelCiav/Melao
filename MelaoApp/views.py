# Importaciones necesarias para las vistas
from django.shortcuts import render # Para renderizar plantillas HTML
from django.http import HttpResponse # Para devolver respuestas HTTP simples (texto, etc.)

# --- Funciones de Vista para MelaoApp ---

# 1. Vista de inicio (Home Page de la aplicación)
# Se accede, por ejemplo, a través de http://127.0.0.1:8000/melaoapp/
# ~/Universidad/ATI/Proyecto/Melao/MelaoApp/views.py

# from django.http import HttpResponse # Ya no lo necesitas si solo renderizas templates

def home(request):
    # Renderiza el template. La ruta es relativa a la carpeta 'templates' de la app.
    # Si lo moviste a MelaoApp/templates/MelaoApp/Melao.html, la ruta es 'MelaoApp/Melao.html'
    return render(request, 'MelaoApp/Melao.html', {})
    # El tercer argumento es un diccionario de contexto, puedes pasar datos al template aquí.
    # Por ejemplo: return render(request, 'MelaoApp/Melao.html', {'nombre': 'Usuario'})

# Puedes añadir más vistas aquí

def index(request):
    """
    Vista que devuelve un mensaje simple para la página de inicio de MelaoApp.
    """
    return HttpResponse("¡Hola desde la vista de inicio de MelaoApp!")

# 2. Vista "Acerca de"
# Se accede, por ejemplo, a través de http://127.0.0.1:8000/melaoapp/about/
def about(request):
    """
    Vista que devuelve un mensaje para la página "Acerca de" de MelaoApp.
    """
    return HttpResponse("Esta es la página 'Acerca de' de mi aplicación MelaoApp.")

# 3. Vista con un parámetro (ejemplo: mostrar detalles de un producto por ID)
# Se accede, por ejemplo, a través de http://127.0.0.1:8000/melaoapp/productos/1/
# El 'id_producto' se captura de la URL como un número entero.
def ver_producto(request, id_producto):
    """
    Vista que muestra un mensaje con el ID del producto recibido como parámetro en la URL.
    """
    # En una aplicación real, aquí buscarías el producto en una base de datos
    # y lo pasarías a un template para mostrar sus detalles.
    return HttpResponse(f"Mostrando detalles del producto con ID: {id_producto}")

# 4. Ejemplo de vista renderizando un template HTML (la forma más común en Django)
# Se accede, por ejemplo, a través de http://127.0.0.1:8000/melaoapp/lista/
def lista_productos(request):
    """
    Vista que prepara una lista de productos y la renderiza usando un template HTML.
    """
    productos = [
        {'nombre': 'Laptop', 'precio': 1200, 'descripcion': 'Portátil de alto rendimiento'},
        {'nombre': 'Mouse', 'precio': 25, 'descripcion': 'Ratón óptico inalámbrico'},
        {'nombre': 'Teclado', 'precio': 75, 'descripcion': 'Teclado mecánico retroiluminado'},
        {'nombre': 'Monitor', 'precio': 300, 'descripcion': 'Monitor Full HD de 27 pulgadas'},
    ]
    
    # El diccionario 'context' se pasa al template.
    # Las claves de este diccionario serán las variables accesibles en el template.
    context = {
        'titulo': 'Lista de Productos Electrónicos',
        'productos': productos,
        'fecha_actual': '27 de Junio de 2025' # Ejemplo de otra variable
    }
    
    # La función render() busca el template en 'templates/MelaoApp/lista_productos.html'
    # dentro del directorio de la aplicación MelaoApp.
    return render(request, 'MelaoApp/templates/Melao.html', context)