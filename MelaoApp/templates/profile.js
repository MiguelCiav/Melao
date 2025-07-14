let dataDummy = [
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
        postDescription: "Alrededor de las 7 PM, nos reuniremos en la biblioteca.",
        lastConnection: "2d",
        likes: 12,
        comments: 5
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
        postDescription: "ATI es lo más duro del planeta chamo.",
        lastConnection: "1d",
        likes: 25,
        comments: 10
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
        postDescription: "Alrededor de las 7 PM, nos reuniremos en la biblioteca.",
        lastConnection: "2d",
        likes: 12,
        comments: 5
    },
    {
        name: "Ethan Hunt",
        image: "/MelaoApp/resources/EthanHuntProfile.png",
        postDescription: "ATI es lo más duro del planeta chamo.",
        lastConnection: "1d",
        likes: 25,
        comments: 10
    }
];

function renderProfileImage(image){
    document.getElementById("ProfileName").innerText = "Ethan Hunt";
    document.getElementById("ProfileImage").setAttribute("src", image);
}

function renderPosts(posts) {
    document.getElementsByClassName("Posts");
    posts.forEach(element => {
        const postDiv = document.createElement("div");
        postDiv.setAttribute("class", "ProfilePost");

        const postImg = document.createElement("img");
        postImg.setAttribute("src", element.image);
        postImg.setAttribute("width", "70");
        postImg.setAttribute("height", "70");
        postImg.setAttribute("alt", "X");

        const postName = document.createElement("p");
        postName.setAttribute("class", "PersonName");
        postName.innerText = element.name;

        const postDescription = document.createElement("p");
        postDescription.setAttribute("class", "PostDescription");
        postDescription.innerText = element.postDescription;

        const postLastConnection = document.createElement("p");
        postLastConnection.setAttribute("class", "LastConnection");
        postLastConnection.innerText = element.lastConnection;

        const postLikes = document.createElement("div");
        postLikes.setAttribute("class", "PostLikes");

        const likeImg = document.createElement("img");
        likeImg.setAttribute("src", "/MelaoApp/resources/Like.png");
        likeImg.setAttribute("width", "20");
        likeImg.setAttribute("height", "20");

        const likesCount = document.createElement("p");
        likesCount.setAttribute("class", "LikesCount");
        likesCount.innerText = element.likes;

        const postComments = document.createElement("div");
        postComments.setAttribute("class", "PostComments");
        const commentImg = document.createElement("img");
        commentImg.setAttribute("src", "/MelaoApp/resources/Comment.png");
        commentImg.setAttribute("width", "20");
        commentImg.setAttribute("height", "20");
        const commentsCount = document.createElement("p");
        commentsCount.setAttribute("class", "CommentsCount");
        commentsCount.innerText = element.comments;

        postDiv.appendChild(postImg);
        postDiv.appendChild(postName);
        postDiv.appendChild(postDescription);
        postDiv.appendChild(postLastConnection);
        postLikes.appendChild(likeImg);
        postLikes.appendChild(likesCount);
        postComments.appendChild(commentImg);
        postComments.appendChild(commentsCount);
        postDiv.appendChild(postLikes);
        postDiv.appendChild(postComments);
        document.getElementsByClassName("Posts")[0].appendChild(postDiv);
    });
}

document.addEventListener("DOMContentLoaded", function() {
    renderPosts(dataDummy);
    renderProfileImage("/MelaoApp/resources/EthanHuntProfile.png");
});