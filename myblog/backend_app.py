# myblog/backend_app.py
from flask import Flask, request, jsonify
from flask_wtf.csrf import CSRFProtect
from functools import wraps
from datetime import datetime
import os
import mysql.connector
import bcrypt
import jwt
from myblog import app, limiter

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Database setup
DATABASE_CONFIG = app.config['DATABASE_CONFIG']

def init_db():
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        username VARCHAR(255) UNIQUE NOT NULL,
                        password VARCHAR(255) NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        title VARCHAR(255) NOT NULL,
                        content TEXT NOT NULL,
                        author VARCHAR(255) NOT NULL,
                        date DATE NOT NULL)''')
    conn.commit()
    cursor.close()
    conn.close()

init_db()

# User Registration and Authentication
@app.route('/api/register', methods=['POST'])
@csrf.exempt  # Exempt CSRF protection for API endpoints if necessary
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    try:
        conn = mysql.connector.connect(**DATABASE_CONFIG)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
    except mysql.connector.IntegrityError:
        return jsonify({"error": "User already exists"}), 400
    finally:
        cursor.close()
        conn.close()
    
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/api/login', methods=['POST'])
@csrf.exempt  # Exempt CSRF protection for API endpoints if necessary
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
        token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({"token": token}), 200
    
    return jsonify({"error": "Invalid credentials"}), 401

# Token-based login required decorator
def login_required(f):
    @wraps(f)
    def check_credentials(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Unauthorized"}), 403
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 403
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 403
        return f(*args, **kwargs)
    return check_credentials

# Pagination and sorting for posts
@app.route('/api/v1/posts', methods=['GET'])
@limiter.limit("5 per minute")
def get_posts_v1():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))
    sort_field = request.args.get('sort', 'date')
    sort_direction = request.args.get('direction', 'asc')

    if page < 1 or per_page < 1:
        return jsonify({"error": "Invalid pagination parameters"}), 400

    conn = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM posts ORDER BY {sort_field} {'DESC' if sort_direction == 'desc' else 'ASC'}")
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    
    total_posts = len(posts)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_posts = posts[start:end]

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
    query = request.args.get('query', '').lower()
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM posts WHERE LOWER(title) LIKE %s OR LOWER(content) LIKE %s OR LOWER(author) LIKE %s OR date LIKE %s", 
                   (f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%'))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(results)

# Create a new post
@app.route('/api/v1/posts', methods=['POST'])
@login_required
@limiter.limit("5 per minute")
def add_post():
    data = request.json
    title = data.get('title')
    content = data.get('content')
    author = data.get('author', 'Anonymous')
    
    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400
    
    date = datetime.now().strftime('%Y-%m-%d')
    
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (title, content, author, date) VALUES (%s, %s, %s, %s)", (title, content, author, date))
    conn.commit()
    post_id = cursor.lastrowid
    cursor.close()
    conn.close()
    
    return jsonify({"id": post_id, "title": title, "content": content, "author": author, "date": date}), 201

# Update an existing post
@app.route('/api/v1/posts/<int:post_id>', methods=['PUT'])
@login_required
@limiter.limit("5 per minute")
def update_post(post_id):
    data = request.json
    title = data.get('title')
    content = data.get('content')
    author = data.get('author')
    date = data.get('date')
    
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM posts WHERE id = %s", (post_id,))
    post = cursor.fetchone()
    if not post:
        cursor.close()
        conn.close()
        return jsonify({"error": "Post not found"}), 404
    
    cursor.execute("UPDATE posts SET title = %s, content = %s, author = %s, date = %s WHERE id = %s", 
                   (title or post['title'], content or post['content'], author or post['author'], date or post['date'], post_id))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"id": post_id, "title": title or post['title'], "content": content or post['content'], "author": author or post['author'], "date": date or post['date']})

# Delete a post
@app.route('/api/v1/posts/<int:post_id>', methods=['DELETE'])
@login_required
@limiter.limit("5 per minute")
def delete_post(post_id):
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM posts WHERE id = %s", (post_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Post deleted"}), 200