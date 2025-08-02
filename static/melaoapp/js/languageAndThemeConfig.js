// static/js/languageAndThemeConfig.js (ubicación probable en tu proyecto Django)

document.addEventListener('DOMContentLoaded', () => {
    const lightModeButton = document.getElementById('LightMode');
    const darkModeButton = document.getElementById('DarkMode');

    // Función para enviar la solicitud a la vista de Django
    const sendThemePreferenceToDjango = (theme) => {
        // Construimos la URL con el parámetro 'theme'
        // Asumiendo que tu URL para set_theme es '/set-theme/' o '/melaoapp/set-theme/'
        // Ajusta la URL según la que hayas definido en tu urls.py
        const url = `/set-theme/?theme=${theme}`; // Ejemplo: /melaoapp/set-theme/
        
        // Simplemente redirigimos el navegador. Django hará la magia de la cookie y la recarga.
        window.location.href = url;
    };

    if (lightModeButton) {
        lightModeButton.addEventListener('click', () => {
            sendThemePreferenceToDjango('light');
        });
    }

    if (darkModeButton) {
        darkModeButton.addEventListener('click', () => {
            sendThemePreferenceToDjango('dark');
        });
    }

    // *** IMPORTANTE: Elimina la lógica de `applyTheme` y `localStorage` de este JS. ***
    // Django se encargará de leer la cookie y aplicar la clase en el HTML que envía al navegador.
    // La parte de la imagen BackArrow ahora se maneja directamente en la plantilla HTML con un condicional de Django.
});