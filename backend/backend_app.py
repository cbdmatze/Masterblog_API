from flask import Flask, request, jsonify
from functools import wraps
from datetime import datetime
import json
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)


# Simple in-memory user store and token store
USERS = {}
TOKENS = {}


# File for persistent post storage
FILE_PATH = 'posts.json'


# Initialize rate limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)


# Load and save posts from JSON file for persistence
def load_posts():
    """Loads posts from a JSON file if it exists, otherwise returns an empty list."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []


def save_posts(posts):
    """Saves the current list of posts to the JSON file."""
    with open(FILE_PATH, 'w') as file:
        json.dump(posts, file)

POSTS = load_posts()


# User Registration and Authentication
@app.route('/api/register', methods=['POST'])
def register():
    """
    Registers a new user by saving their username and password.
    
    Returns an error if the username already exists.
    """
    data = request.json
    username = data['username']
    password = data['password']
    
    if username in USERS:
        return jsonify({"error": "User already exists"}), 400
    
    USERS[username] = password
    return jsonify({"message": "User registered successfully"}), 201


@app.route('/api/login', methods=['POST'])
def login():
    """
    Logs in a user by verifying their credentials and returns an authorization token.
    
    Returns an error if the credentials are invalid.
    """
    data = request.json
    username = data['username']
    password = data['password']
    
    if USERS.get(username) == password:
        token = f"token_{username}"
        TOKENS[token] = username
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401


# Token-based login required decorator
def login_required(f):
    """Decorator function to require a valid login token for protected routes."""
    @wraps(f)
    def check_credentials(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token not in TOKENS:
            return jsonify({"error": "Unauthorized"}), 403
        return f(*args, **kwargs)
    return check_credentials


# Pagination and sorting for posts
@app.route('/api/v1/posts', methods=['GET'])
@limiter.limit("5 per minute")
def get_posts_v1():
    """
    Retrieves a paginated and optionally sorted list of blog posts.
    
    Supports pagination with 'page' and 'per_page' parameters, as well as sorting
    by any field with 'sort' and 'direction' (asc or desc).
    """
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))
    sort_field = request.args.get('sort', 'date')
    sort_direction = request.args.get('direction', 'asc')

    total_posts = len(POSTS)
    start = (page - 1) * per_page
    end = start + per_page

    sorted_posts = sorted(POSTS, key=lambda x: x.get(sort_field, ''), reverse=(sort_direction == 'desc'))
    paginated_posts = sorted_posts[start:end]

    return jsonify({
        "total_posts": total_posts,
        "page": page,
        "per_page": per_page,
        "posts": paginated_posts
    })


# Search functionality for posts
@app.route('/api/v1/posts/search', methods=['GET'])
@limiter.limit("5 per minute")
def search_posts():
    """
    Searches posts by title, content, author, or date using a query string.
    
    Returns posts that match the search query.
    """
    query = request.args.get('query', '').lower()
    results = [
        post for post in POSTS
        if query in post['title'].lower() or
           query in post['content'].lower() or
           query in post['author'].lower() or
           query in post['date']
    ]
    return jsonify(results)


# Create a new post
@app.route('/api/v1/posts', methods=['POST'])
@login_required
@limiter.limit("5 per minute")
def add_post():
    """
    Adds a new blog post. Requires a valid login token.
    
    Returns the created post.
    """
    data = request.json
    new_post = {
        "id": max(post['id'] for post in POSTS) + 1 if POSTS else 1,
        "title": data['title'],
        "content": data['content'],
        "author": data.get('author', 'Anonymous'),
        "date": datetime.now().strftime('%Y-%m-%d')
    }
    POSTS.append(new_post)
    save_posts(POSTS)
    return jsonify(new_post), 201


# Update an existing post
@app.route('/api/v1/posts/<int:post_id>', methods=['PUT'])
@login_required
@limiter.limit("5 per minute")
def update_post(post_id):
    """
    Updates an existing post. Requires a valid login token.
    
    Returns the updated post or an error if the post was not found.
    """
    data = request.json
    for post in POSTS:
        if post['id'] == post_id:
            post['title'] = data.get('title', post['title'])
            post['content'] = data.get('content', post['content'])
            post['author'] = data.get('author', post['author'])
            post['date'] = data.get('date', post['date'])
            save_posts(POSTS)
            return jsonify(post)
    return jsonify({"error": "Post not found"}), 404


# Delete a post
@app.route('/api/v1/posts/<int:post_id>', methods=['DELETE'])
@login_required
@limiter.limit("5 per minute")
def delete_post(post_id):
    """
    Deletes a post by its ID. Requires a valid login token.
    
    Returns a success message or an error if the post was not found.
    """
    global POSTS
    POSTS = [post for post in POSTS if post['id'] != post_id]
    save_posts(POSTS)
    return jsonify({"message": "Post deleted"}), 200


# Run Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
