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

document.addEventListener("DOMContentLoaded", function() {
    renderPeople(dataDummy);
});