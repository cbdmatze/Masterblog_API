from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app) # Enable CORS for all routes


POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


# GET Endpoint to Retrieve All Posts
@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)


# POST Endpoint to Add a Nwe Book
@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.json

    # Ceck if title and content are provided
    if not data or 'title' not in data or 'content' not in data:
        missing_fields = []
        if 'title' not in data:
            missing_fields.append('title')
        if 'content' not in data:
            missing_fields.append('content')
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
    
    # Create new post with auto-incremented ID
    new_id = max(post['id'] for post in POSTS) + 1 if POSTS else 1
    new_post = {
        "id": new_id, 
        "title": data['title'],
        "content": data['content']
    }

    POSTS.append(new_post)

    return jsonify(new_post), 201


# DELETE Endpoint to Remove a Post by ID
@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    # Find the post by id
    post = next((post for post in POSTS if post['id'] == id), None)

    # If the post is not found, return 404
    if post is None:
        return jsonify({"error": "Post not found"})
    
    # Remove the post from the list
    POSTS.remove(post)

    return jsonify({"message": f"Post with id {id} has been deleted"}), 200


# PUT Endpoint to Update an Existing Post
@app.route('/api/posts/<int:id>', methods=['PUT'])
def update_post(id):
    data = request.json

    # Find the post by id
    post = next((post for post in POSTS if post['id'] == id), None)

    if post is None:
        return jsonify({"error": "Post not found"}), 404
    
    # Update title and/or content if provided
    post['title'] = data.get('title', post['title'])
    post['content'] = data.get('content', post['content'])

    return jsonify(post), 200


# GET Endpoint to Search Posts by Title or Content
@app.route('/api/posts/search', methods=['GET'])
def search_post():
    title_query = request.args.get('title', '')
    content_query = request.args.get('content', '')

    # Filter posts based on search queries
    results = [
        post for post in POSTS
        if title_query.lower() in post['title'].lower() or content_query.lower() in post['content'].lower()
    ]

    return jsonify(results), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)
    