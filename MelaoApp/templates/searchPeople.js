let dataDummy = [
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
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

        const addFriends = document.createElement("img");
        addFriends.setAttribute("src", "/MelaoApp/resources/AddFriend.png");
        addFriends.setAttribute("width", "30");
        addFriends.setAttribute("height", "30");
        addFriends.setAttribute("alt", "AddFriend");
        addFriends.setAttribute("class", "Icon");

        const chat = document.createElement("img");
        chat.setAttribute("src", "/MelaoApp/resources/Chat.png");
        chat.setAttribute("width", "30");
        chat.setAttribute("height", "30");
        chat.setAttribute("alt", "Chat");
        chat.setAttribute("class", "Icon");

        personDiv.appendChild(personImg);
        personDiv.appendChild(personName);
        personDiv.appendChild(addFriends);
        personDiv.appendChild(chat);

        document.getElementsByClassName("SearchPannel")[0].appendChild(personDiv);
    });
}

function setTheme(){
    const body = document.body;
    const BackArrow = document.getElementById('Arrow-button');
    const Person = document.getElementsByClassName('PersonDiv');

    const applyTheme = (theme) => {
        if (theme === 'dark') {
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
            BackArrow.querySelector('img').src = '/MelaoApp/resources/DarkMode/BackArrow.png';
            Array.from(Person).forEach(el => {
                const addFriend = el.querySelector('img[alt="AddFriend"]');
                const chat = el.querySelector('img[alt="Chat"]');

                if (addFriend) addFriend.src = '/MelaoApp/resources/DarkMode/AddFriend.png';
                
                if (chat) chat.src = '/MelaoApp/resources/DarkMode/Chat.png';
            
            });    
        } else {
            body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
            BackArrow.querySelector('img').src = '/MelaoApp/resources/BackArrow.png';
            Array.from(Person).forEach(el => {
                const addFriend = el.querySelector('img[alt="AddFriend"]');
                const chat = el.querySelector('img[alt="Chat"]');

                if (addFriend) addFriend.src = '/MelaoApp/resources/AddFriend.png';
                
                if (chat) addFriend.src = '/MelaoApp/resources/Chat.png';
            
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
    renderPeople(dataDummy);
    setTheme();
});