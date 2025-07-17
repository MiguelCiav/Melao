let dataDummy = [
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
        description: "Envió petición de amistad",
        notificationIcon: "/MelaoApp/resources/AddFriendBGLess.png"
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
        description: "Envió petición de chat",
        notificationIcon: "/MelaoApp/resources/chatRequest.png"
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
        description: "Comentó tu publicación",
        notificationIcon: "/MelaoApp/resources/Comment.png"
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

        const description = document.createElement("p");
        description.setAttribute("class", "Description");
        description.innerText = element.description;

        const notificationIcon = document.createElement("img");
        notificationIcon.setAttribute("src", element.notificationIcon);
        notificationIcon.setAttribute("width", "30");
        notificationIcon.setAttribute("height", "30");
        notificationIcon.setAttribute("alt", "X");
        notificationIcon.setAttribute("class", "NotificationIcon");

        personDiv.appendChild(personImg);
        personDiv.appendChild(personName);
        personDiv.appendChild(description);
        personDiv.appendChild(notificationIcon);

        document.getElementsByClassName("NotificationsPannel")[0].appendChild(personDiv);
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