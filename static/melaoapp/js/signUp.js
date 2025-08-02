function setTheme(){
    const body = document.body;

    const applyTheme = (theme) => {
        if (theme === 'dark') {
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
            
        } else {
            body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
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