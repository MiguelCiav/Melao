function setTheme(){
    const BackArrow = document.getElementById('Arrow-button');

    const applyTheme = (theme) => {
        if (theme === 'dark') {
            BackArrow.querySelector('img').src = '/MelaoApp/resources/DarkMode/BackArrow.png';
            
        } else {
            BackArrow.querySelector('img').src = '/MelaoApp/resources/BackArrow.png';
        }
    };
    
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        applyTheme(savedTheme);
    } else {
        applyTheme('light');
    }
}

document.addEventListener("DOMContentLoaded", function() {
    setTheme();
});