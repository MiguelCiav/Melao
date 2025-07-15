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

document.addEventListener("DOMContentLoaded", function() {
    renderPeople(dataDummy);
});