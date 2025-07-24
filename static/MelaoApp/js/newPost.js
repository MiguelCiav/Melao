function setTheme(){
    const body = document.body;
    const Xicon = document.getElementById('X-Icon');

    const applyTheme = (theme) => {
        if (theme === 'dark') {
            Xicon.querySelector('img').src = '/MelaoApp/resources/DarkMode/X-Icon.png';
        } else {
            Xicon.querySelector('img').src = '/MelaoApp/resources/X-Icon.png';
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