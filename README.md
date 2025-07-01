![Melao Banner](https://i.imgur.com/5rlf5qT.png)

# 📌 Melao
Melao es una plataforma social exclusiva para estudiantes de Aplicaciones con la Tecnología Internet (ATI) de la Universidad Central de Venezuela, Facultad de Ciencias, Escuela de Computación. 
Conéctate con tus compañeros, comparte experiencias y mantente al día con lo que sucede en la comunidad ATI.

Este proyecto nace de la iniciativa del grupo docente de Aplicaciones con la Tecnología Internet para que los estudiantes desarrollen una aplicación web que cumpla con los objetivos de la materia. Nuestro enfoque es la creación de una red social dinámica y fácil de usar, donde los estudiantes de ATI puedan interactuar y compartir conocimientos.

## 👥 Equipo de Desarrolladores

+ [Cao Carlos](https://github.com/CaoCarlos55)
+ [Carios César](https://github.com/brankarios)
+ [Ciavato Miguel](https://github.com/MiguelCiav)
+ [Homsany Jhonatan](https://github.com/JhonatanHZ)
+ [Reis Erimar](https://github.com/wholood)
+ [Rodríguez Luis](https://github.com/)

## ✨ Características Principales

Melao ofrece una variedad de funcionalidades para enriquecer la experiencia del usuario:

* **Perfiles de Usuario**: Cada usuario tendrá un perfil personalizable con su información.
* **Muro Personal**: Publica tus pensamientos, experiencias, y contenido multimedia (videos, audios, fotos, enlaces). Las publicaciones pueden ser públicas o privadas (solo para amigos).
* **Comentarios y Respuestas**: Interactúa con las publicaciones de otros usuarios dejando comentarios y respondiendo a los mismos.
* **Sistema de Amigos**: Sigue a otros usuarios, envía y acepta solicitudes de amistad. Podrás buscar amigos fácilmente.
* **Chat en Tiempo Real**: Comunícate con otros usuarios a través de un chat privado.
* **Notificaciones**: Mantente informado sobre nuevos mensajes de chat, comentarios en tus publicaciones y amigos conectados. Las notificaciones también pueden enviarse por correo electrónico.
* **Recuperación de Contraseña**: Restablece tu contraseña fácilmente a través de tu correo electrónico registrado. 
* **Diseño Adaptativo**: Accede a la aplicación desde cualquier dispositivo. 
* **Internacionalización**: El sistema podrá visualizarse en distintos idiomas.
* **Personalización**: Cambia el color de tu perfil y muro, y activa el modo oscuro. 

## 🚀 Fases del Proyecto

El desarrollo de Melao se realizará siguiendo una adaptación de la metodología ágil Scrum, utilizando GitHub para la gestión del proyecto. El proyecto está dividido en las siguientes fases:

| Fase         | Fecha de Entrega |
| :----------- | :--------------- |
| Inception    | 01 julio 2025    |
| Design       | 15 julio 2025    |
| Construction | 07 agosto 2025   |

## 📋Modelo de Casos de Uso
![Casos de Uso Melao](https://i.imgur.com/Pr51vVd.png)

## 🛠️ Tecnologías Utilizadas

* **Lenguaje**: Python
* **Framework Web**: Django 5.0.6
* **Base de Datos**: SQLite
* **Control de Versiones**: Git y GitHub

## 📂Versionado  
Este proyecto usa [SemVer](https://semver.org/). Para ver los cambios, consulta el [CHANGELOG.md](CHANGELOG.md).  

## 🗄️Ramas  
- main → Producción.  
- feature/* → Nuevas funcionalidades.

## 🐳 Cómo Usar Melao

Este proyecto incluye un Dockerfile para facilitar el despliegue y la ejecución de la aplicación en un entorno contenedorizado. Sigue estos pasos para construir la imagen y ejecutar el contenedor:

### Prerequisitos

Asegúrate de tener Docker instalado en tu sistema. Si no lo tienes, puedes descargarlo desde el [sitio oficial de Docker](https://www.docker.com/get-started).

### Pasos para Usar Docker

1.  **Clonar el Repositorio:**
    Si aún no lo has hecho, clona el repositorio del proyecto en tu máquina local:

    ```bash
    git clone https://github.com/MiguelCiav/Melao.git
    cd Melao
    ```

2.  **Construir la Imagen Docker:**
    Navega al directorio raíz del proyecto donde se encuentra el `Dockerfile` y ejecuta el siguiente comando para construir la imagen. Asignaremos un nombre a la imagen (por ejemplo, `melao-app`):

    ```bash
    docker build -t melao-app .
    ```
    

3.  **Ejecutar el Contenedor Docker:**
    Una vez que la imagen ha sido construida exitosamente, puedes ejecutar un contenedor a partir de ella.

    ```bash
    docker run -p 8000:8000 --name melao-container melao-app
    ```

4.  **Acceder a la Aplicación:**
    Una vez que el contenedor esté en ejecución, la aplicación estará accesible en tu navegador web en:

    ```
    http://localhost:8000
    ```
