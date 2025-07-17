let dataDummy = [
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
        lastConnection: "Activo ahora"
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
        lastConnection: "Activo hace 2d"
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
        lastConnection: "Activo hace 5 min"
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
        lastConnection: "Activo hace 2h"
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
        lastConnection: "Activo hace 1 semana"
    }
];

function renderPeople(people) {
    people.forEach(element => {
        const personDiv = document.createElement("div");
        personDiv.setAttribute("class", "PersonDiv");

        const personImg = document.createElement("img");
        personImg.setAttribute("src", element.image);
        personImg.setAttribute("width", "70");
        personImg.setAttribute("height", "70");
        personImg.setAttribute("alt", "X");

        const personName = document.createElement("p");
        personName.setAttribute("class", "PersonName");
        personName.innerText = element.name;

        const personLastConnection = document.createElement("p");
        personLastConnection.setAttribute("class", "LastConnection");
        personLastConnection.innerText = element.lastConnection;

        personDiv.appendChild(personImg);
        personDiv.appendChild(personName);
        personDiv.appendChild(personLastConnection);

        document.getElementsByClassName("ChatsPannel")[0].appendChild(personDiv);
    });
}
function setTheme(){
    const body = document.body;
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
}
document.addEventListener("DOMContentLoaded", function() {
    renderPeople(dataDummy);
    setTheme();
});