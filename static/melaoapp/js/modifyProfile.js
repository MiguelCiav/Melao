function setTheme(){
    const BackArrow = document.getElementById('Arrow-button');
    const RightArrow = document.getElementsByClassName('option-container');

    const applyTheme = (theme) => {
        if (theme === 'dark') {
            BackArrow.querySelector('img').src = '/melaoapp/resources/DarkMode/BackArrow.png';
            Array.from(RightArrow).forEach(el => {
                const img = el.querySelector('img');
                if (img) img.src = '/melaoapp/resources/DarkMode/right_arrow.png';
            });
            
        } else {
            BackArrow.querySelector('img').src = '/melaoapp/resources/BackArrow.png';
            Array.from(RightArrow).forEach(el => {
                const img = el.querySelector('img');
                if (img) img.src = '/melaoapp/resources/right_arrow.svg';
            });
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