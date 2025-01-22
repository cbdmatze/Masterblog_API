function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrfToken = getCookie('csrf_token');

fetch('http://127.0.0.1:5002/register', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
    },
    body: JSON.stringify({ username: 'siggi', password: '12345' })
})
.then(response => {
    if (!response.ok) {
        throw new Error('Failed to register.');
    }
    return response.json();
})
.then(data => {
    console.log('User registered:', data);
})
.catch(error => {
    console.error('Error:', error);
});