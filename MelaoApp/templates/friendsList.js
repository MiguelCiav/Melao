let dataDummy = [
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png"
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png"
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png"
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png"
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png"
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

        const deleteFriend = document.createElement("img");
        deleteFriend.setAttribute("src", "/MelaoApp/resources/X-Search-Icon-Filled.png");
        deleteFriend.setAttribute("width", "30");
        deleteFriend.setAttribute("height", "30");
        deleteFriend.setAttribute("alt", "X");
        deleteFriend.setAttribute("class", "DeleteFriendIcon");

        personDiv.appendChild(personImg);
        personDiv.appendChild(personName);
        personDiv.appendChild(deleteFriend);

        document.getElementsByClassName("FriendsPannel")[0].appendChild(personDiv);
    });
}

document.addEventListener("DOMContentLoaded", function() {
    renderPeople(dataDummy);
});