// Function that runs once the window is fully loaded
window.onload = function() {
    var savedBaseUrl = localStorage.getItem('apiBaseUrl');
    if (savedBaseUrl) {
        document.getElementById('api-base-url').value = savedBaseUrl;
        loadPosts();
    }
}

// Function to fetch all the posts from the API and display them on the page
function loadPosts() {
    var baseUrl = document.getElementById('api-base-url').value;
    localStorage.setItem('apiBaseUrl', baseUrl);

    fetch(baseUrl + '/api/v1/posts')
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to fetch posts.");
            }
            return response.json();
        })
        .then(data => {
            const postContainer = document.getElementById('post-container');
            postContainer.innerHTML = '';

            data.posts.forEach(post => {
                const postDiv = document.createElement('div');
                postDiv.className = 'post';
                postDiv.innerHTML = `<h2>${post.title}</h2><p>${post.content}</p>
                <button onclick="deletePost(${post.id})">Delete</button>`;
                postContainer.appendChild(postDiv);
            });
        })
        .catch(error => {
            console.error('Error loading posts:', error);
            alert('Error loading posts: ' + error.message);
        });
}

// Function to send a POST request to the API to add a new post
function addPost() {
    var baseUrl = document.getElementById('api-base-url').value;
    var postTitle = document.getElementById('post-title').value;
    var postContent = document.getElementById('post-content').value;

    if (!postTitle || !postContent) {
        alert("Title and content cannot be empty!");
        return;
    }

    // Sanitize input
    postTitle = postTitle.replace(/</g, "&lt;").replace(/>/g, "&gt;");
    postContent = postContent.replace(/</g, "&lt;").replace(/>/g, "&gt;");

    fetch(baseUrl + '/api/v1/posts', {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrf_token')  // Include CSRF token
        },
        body: JSON.stringify({ title: postTitle, content: postContent })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to add post.");
        }
        return response.json();
    })
    .then(post => {
        console.log('Post added:', post);
        loadPosts();
    })
    .catch(error => {
        console.error('Error adding post:', error);
        alert('Error adding post: ' + error.message);
    });
}

// Function to send a DELETE request to the API to delete a post
function deletePost(postId) {
    var baseUrl = document.getElementById('api-base-url').value;

    fetch(baseUrl + '/api/v1/posts/' + postId, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': getCookie('csrf_token')  // Include CSRF token
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to delete post.");
        }
        console.log('Post deleted:', postId);
        loadPosts();
    })
    .catch(error => {
        console.error('Error deleting post:', error);
        alert('Error deleting post: ' + error.message);
    });
}

// Function to get a cookie value by name
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