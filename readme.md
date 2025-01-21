# REDUNDANT THINGS OF PARAMOUNT IMPORTANCE

## Overview

Welcome to the **REDUNDANT THINGS OF PARAMOUNT IMPORTANCE** blog, where we showcase posts that seem trivial yet have profound importance! This blog application allows users to register, login, create, update, delete, and browse blog posts using a simple RESTful API.

The backend is powered by Flask, with features such as rate limiting, user authentication, pagination, sorting, and search functionality. The frontend allows users to interact with the API in a simple, user-friendly interface.

## Features

- **User Registration & Login**: Users can register and log in to create posts.
- **Rate Limiting**: Limits requests to prevent abuse.
- **Create, Read, Update, Delete (CRUD)**: Full CRUD functionality for blog posts.
- **Pagination**: View blog posts in pages.
- **Sorting**: Sort blog posts by date, title, or author.
- **Search**: Search blog posts by title, content, author, or date.
- **Persistence**: Posts are saved in a JSON file to ensure they persist between sessions.

## API Endpoints

### User Authentication

- **POST /api/register**: Register a new user.
- **POST /api/login**: Log in and get an authentication token.

### Blog Posts

- **GET /api/v1/posts**: Retrieve a paginated list of posts (with optional sorting).
- **GET /api/v1/posts/search**: Search posts by query.
- **POST /api/v1/posts**: Create a new post (requires login).
- **PUT /api/v1/posts/{id}**: Update a post (requires login).
- **DELETE /api/v1/posts/{id}**: Delete a post (requires login).

## Running the Project

1. Clone the repository.
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database configuration in `config.py`.
4. Run the application:

    ```bash
    python run.py
    ```

## Configuration

Ensure you have a `config.py` file with the following structure:

```python
DATABASE_CONFIG = {
    'user': 'your_db_user',
    'password': 'your_db_password',
    'host': 'your_db_host',
    'database': 'your_db_name'
}

SECRET_KEY = 'your_secret_key'

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Flask
MySQL Connector/Python
bcrypt
PyJWT
Flask-Limiter
Enjoy blogging with REDUNDANT THINGS OF PARAMOUNT IMPORTANCE!


This [readme.md](http://_vscodecontentref_/4) provides a comprehensive overview of your application, its features, API endpoints, setup instructions, and acknowledgements.
