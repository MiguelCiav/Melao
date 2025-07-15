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

document.addEventListener("DOMContentLoaded", function() {
    renderPeople(dataDummy);
});