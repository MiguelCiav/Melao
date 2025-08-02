document.addEventListener('DOMContentLoaded', () => {
    const lightModeButton = document.getElementById('LightMode');
    const darkModeButton = document.getElementById('DarkMode');
    const sendThemePreferenceToDjango = (theme) => {
        const url = `/set-theme/?theme=${theme}`;
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
});