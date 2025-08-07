const csrfToken = CSRF_TOKEN; 
const senderUsername = SENDER_USERNAME;
const url = ADD_FRIEND_URL;

const acceptFriendRequest = (sender_user) => {
    const data = {
        sender: sender_user
    };

    console.log(data.sender);

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