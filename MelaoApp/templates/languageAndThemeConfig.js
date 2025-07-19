
document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const lightModeButton = document.getElementById('LightMode');
    const darkModeButton = document.getElementById('DarkMode');
    const BackArrow = document.getElementById('Arrow-button');

    const applyTheme = (theme) => {
        if (theme === 'dark') {
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
            BackArrow.querySelector('img').src = '/MelaoApp/resources/DarkMode/BackArrow.png';
            
        } else {
            body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
            BackArrow.querySelector('img').src = '/MelaoApp/resources/BackArrow.png';
        }
    };
    
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        applyTheme(savedTheme);
    } else {
        applyTheme('light');
    }

    if (lightModeButton) {
        lightModeButton.addEventListener('click', () => {
            applyTheme('light');
        });
    }

    if (darkModeButton) {
        darkModeButton.addEventListener('click', () => {
            applyTheme('dark');
        });
    }

});