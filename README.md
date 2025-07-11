<img src="https://i.imgur.com/n4Shznw.png" width="830">

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
<img src="https://i.imgur.com/Pr51vVd.png" width="500">

## 📂Versionado  
Este proyecto usa [SemVer](https://semver.org/). Para ver los cambios, consulta el [CHANGELOG.md](CHANGELOG.md).  

## 🗄️Ramas  
- main → Producción.  
- feature/* → Nuevas funcionalidades.

## 📐 Descripción de la Arquitectura

* **Aplicación Web:**
    * Arquitectura cliente-servidor, donde el navegador web del usuario interactúa con un servidor web utilizando el protocolo HTTP/HTTPS para la comunicación.
    * La interfaz de usuario (frontend) será desarrollada utilizando lenguajes estándar de la web: HTML para la estructura, CSS para el estilo y JavaScript para la interactividad.
    * La aplicación debe estar diseñada para alta disponibilidad, permitiendo el acceso 24 horas al día, 7 días a la semana, desde cualquier ubicación geográfica.
    * El diseño general buscará ofrecer una experiencia de usuario intuitiva y un rendimiento adecuado para una aplicación de red social.

* **Aplicación MPA (Multi-Page Application):**
    * El front-end en el lado del cliente se considera ligero o mediano, ya que gran parte del contenido HTML es generado y renderizado en el servidor para cada solicitud.
    * El back-end es "pesado" en el sentido de que es el encargado de procesar la lógica de negocio, interactuar con la base de datos y generar las páginas HTML dinámicamente que son enviadas al navegador.

* **Uso de lenguaje Python y framework Django para el backend:**
    * La lógica de negocio y la gestión de datos del lado del servidor se desarrollan en Python, aprovechando la robustez y las características del framework Django 5.0.6.
    * El código está organizado siguiendo el patrón arquitectónico Modelo-Vista-Template (MVT), que es una variante del patrón Modelo-Vista-Controlador (MVC) adaptada por Django.
        * **Modelos:** Definen la estructura de los datos y la interacción con la base de datos (por ejemplo, para Usuarios, Publicaciones, Mensajes, entre otros).
        * **Vistas:** Contienen la lógica de negocio, procesan las solicitudes HTTP, interactúan con los modelos y seleccionan la plantilla adecuada para renderizar la respuesta.
        * **Templates:** Son archivos HTML que contienen marcadores especiales (lenguaje de plantillas de Django) que permiten inyectar datos dinámicamente generados por las vistas.

* **Base de datos: SQLite:**
    * Se utilizará SQLite como sistema de gestión de bases de datos relacionales. Esto facilita la portabilidad y la configuración inicial al no requerir un servidor de base de datos separado.

* **Servidor web:**
    * Para el entorno de desarrollo, Django incluye un servidor de desarrollo integrado.
    * En un entorno de producción, la aplicación Django será desplegada típicamente en Apache, que actuará como un proxy inverso para servir archivos estáticos directamente y reenviar las solicitudes dinámicas al servidor de aplicaciones que ejecuta Django.

![Arquitectura utilizada](https://i.imgur.com/IXofE8q.png)

## 📋Diagramas del Sistema
### Diagrama de Arquitectura
<img src="https://i.imgur.com/yo3gpRL.png" width="830">

### Diagrama de Despliegue
<img src="https://i.imgur.com/8JuJmH9.png" width="500">

### Diagrama de Paquetes
<img src="https://i.imgur.com/n8UUy8Q.png" width="830">

## 📂Diagramas de Clases de Análisis
### UC Chatear: Fallos en el envío de mensajes
<img src="https://i.imgur.com/4WtCsJy.jpeg" width="500">

### UC Chatear: Problemas con la disponibilidad
<img src="https://i.imgur.com/IuHQIi4.jpeg" width="830">

### UC Publicar en Muro: Validaciones de contenido
<img src="https://i.imgur.com/EV9IdTo.jpeg" width="830">

### UC Comentar: Validaciones de comentarios
<img src="https://i.imgur.com/aoD1Jvi.jpeg" width="500">


