document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('.search-tab input');
    const persons = document.querySelectorAll('.person');

    searchInput.addEventListener('input', function(event) {
        const searchTerm = event.target.value.toLowerCase();
        persons.forEach(person => {
            const personNameElement = person.querySelector('.person_name');
            const personName = personNameElement.textContent.toLowerCase();
            if (personName.startsWith(searchTerm)) {
                person.style.display = 'flex';
            } else {
                person.style.display = 'none';
            }
        });
    });
});

const csrfToken = CSRF_TOKEN; 
const senderUsername = SENDER_USERNAME;
const url = ADD_FRIEND_URL;

const sendFriendRequest = (recipientUsername, notificationType) => {
    const data = {
        recipient_username: recipientUsername,
        sender_username: senderUsername,
        type: notificationType
    };

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(errorData => {
                throw new Error(errorData.message || 'Error en el servidor');
            });
        }
        return response.json();
    })
    .then(data => {
        console.log('Respuesta del servidor:', data);
    });
};