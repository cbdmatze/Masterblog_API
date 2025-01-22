import requests
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Function that runs once the window is fully loaded
def on_window_load():
    saved_base_url = get_local_storage_item('apiBaseUrl')
    if saved_base_url:
        set_input_value('api-base-url', saved_base_url)
        load_posts()

# Function to fetch all the posts from the API and display them on the page
def load_posts():
    base_url = get_input_value('api-base-url')
    set_local_storage_item('apiBaseUrl', base_url)

    response = requests.get(base_url + '/posts')
    if response.status_code != 200:
        raise Exception("Failed to fetch posts.")
    
    data = response.json()
    post_container = get_element_by_id('post-container')
    post_container.innerHTML = ''

    for post in data:
        post_div = create_element('div')
        post_div.className = 'post'
        post_div.innerHTML = f'<h2>{post["title"]}</h2><p>{post["content"]}</p><button onclick="delete_post({post["id"]})">Delete</button>'
        append_child(post_container, post_div)

# Function to send a POST request to the API to add a new post
def add_post():
    base_url = get_input_value('api-base-url')
    post_title = get_input_value('post-title')
    post_content = get_input_value('post-content')

    if not post_title or not post_content:
        alert("Title and content cannot be empty!")
        return

    # Sanitize input
    post_title = post_title.replace('<', "&lt;").replace('>', "&gt;")
    post_content = post_content.replace('<', "&lt;").replace('>', "&gt;")

    headers = {
        'Content-Type': 'application/json',
        'X-CSRFToken': get_cookie('csrf_token')  # Include CSRF token
    }
    body = json.dumps({ 'title': post_title, 'content': post_content })

    response = requests.post(base_url + '/posts', headers=headers, data=body)
    if response.status_code != 201:
        raise Exception("Failed to add post.")
    
    post = response.json()
    print('Post added:', post)
    load_posts()

# Function to send a DELETE request to the API to delete a post
def delete_post(post_id):
    base_url = get_input_value('api-base-url')

    headers = {
        'X-CSRFToken': get_cookie('csrf_token')  # Include CSRF token
    }

    response = requests.delete(base_url + '/posts/' + post_id, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to delete post.")
    
    print('Post deleted:', post_id)
    load_posts()

# Function to get a cookie value by name
def get_cookie(name):
    cookie_value = None
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie.startswith(name + '='):
                cookie_value = cookie[len(name) + 1:]
                break
    return cookie_value

# Mock functions to simulate JavaScript DOM operations
def get_local_storage_item(key):
    # Simulate getting an item from local storage
    return None

def set_local_storage_item(key, value):
    # Simulate setting an item in local storage
    pass

def get_input_value(element_id):
    # Simulate getting the value of an input element
    return "http://localhost:5000"

def set_input_value(element_id, value):
    # Simulate setting the value of an input element
    pass

def get_element_by_id(element_id):
    # Simulate getting a DOM element by ID
    class Element:
        def __init__(self):
            self.innerHTML = ''
    return Element()

def create_element(tag):
    # Simulate creating a new DOM element
    return get_element_by_id('')

def append_child(parent, child):
    # Simulate appending a child element to a parent element
    pass

def alert(message):
    # Simulate an alert dialog
    print("ALERT:", message)

# Simulate window.onload
on_window_load()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)