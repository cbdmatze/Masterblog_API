import unittest
from flask import Flask
from flask_testing import TestCase
import json
from myblog import app, limiter
from myblog.backend_app import init_db  # Import the init_db function from the backend_app module
import jwt
import datetime

class MyBlogTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DATABASE_CONFIG'] = {
            'user': 'root',
            'password': 'Ma-294022275',
            'host': 'localhost',
            'database': 'test_myblog'
        }
        return app
    
    def setUp(self):
        init_db()

    def tearDown(self):
        pass

    def test_register(self):
        response = self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_register_missing_fields(self):
        response = self.client.post('/api/register', data=json.dumps({
            'username': 'testuser'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_register_existing_user(self):
        self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        response = self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_login(self):
        self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        response = self.client.post('/api/login', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', json.loads(response.data))

    def test_login_incorrect_credentials(self):
        self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        response = self.client.post('/api/login', data=json.dumps({
            'username': 'testuser', 
            'password': 'wrongpassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_get_posts(self):
        response = self.client.get('/api/v1/posts')
        self.assertEqual(response.status_code, 200)

    def test_add_post(self):
        self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        login_response = self.client.post('/api/login', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        token = json.loads(login_response.data)['token']
        response = self.client.post('/api/v1/posts', data=json.dumps({
            'title': 'Test Post',
            'content': 'This is a test post.'
        }), headers={'Authorization': f'Bearer {token}'},  content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_add_post_missing_fields(self):
        self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        login_response = self.client.post('/api/login', data=json.dumps({
            'username': 'testuser', 
            'password': 'testpassword'
        }), content_type='application/json')
        token = json.loads(login_response.data)['token']
        response = self.client.post('/api/v1/posts', data=json.dumps({
            'title': 'Test Post'
        }), headers={'Authorization': f'Bearer {token}'}, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_update_post(self):
        self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        login_response = self.client.post('/api/login', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        token = json.loads(login_response.data)['token']
        self.client.post('/api/v1/posts', data=json.dumps({
            'title': 'Test Post',
            'content': 'This is a test post.'
        }), headers={'Authorization': f'Bearer {token}'},  content_type='application/json')
        response = self.client.put('/api/v1/posts/1', data=json.dumps({
            'title': 'Updated Post',
            'content': 'This is an updated post.'
        }), headers={'Authorization': f'Bearer {token}'},  content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_update_non_existing_post(self):
        self.client.post('/api/register', data=json.dumps({
            'username': 'testuser', 
            'password': 'testpassword'
        }), content_type='application/json')
        login_response = self.client.post('/api/login', data=json.dumps({
            'username': 'testuser', 
            'password': 'testpassword'
        }), content_type='application/json')
        token = json.loads(login_response.data)['token']
        response = self.client.put('/api/v1/posts/999', data=json.dumps({
            'title': 'Updated Post',
            'content': 'This is an updated post.'
        }), headers={'Authorization': f'Bearer {token}'}, content_type='application/json')
        self.assertEqual(response.status_code, 404)
    
    def test_update_post_missing_fields(self):
        self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        login_response = self.client.post('/api/login', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        token = json.loads(login_response.data)['token']
        self.client.post('/api/v1/posts', data=json.dumps({
            'title': 'Test Post',
            'content': 'This is a test post.'
        }), headers={'Authorization': f'Bearer {token}'},  content_type='application/json')
        response = self.client.put('/api/v1/posts/1', data=json.dumps({
            'title': 'Updated Post'
        }), headers={'Authorization': f'Bearer {token}'},  content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_delete_post(self):
        self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        login_response = self.client.post('/api/login', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        token = json.loads(login_response.data)['token']
        self.client.post('/api/v1/posts', data=json.dumps({
            'title': 'Test Post',
            'content': 'This is a test post.'
        }), headers={'Authorization': f'Bearer {token}'},  content_type='application/json')
        response = self.client.delete('/api/v1/posts/1', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 200)

    def test_delete_non_existing_post(self):
        self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        login_response = self.client.post('/api/login', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        token = json.loads(login_response.data)['token']
        response = self.client.delete('/api/v1/posts/999', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 404)

    def test_rate_limiting(self):
        self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        login_response = self.client.post('/api/login', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        token = json.loads(login_response.data)['token']
        for _ in range(5):
            response = self.client.post('/api/v1/posts', data=json.dumps({
                'title': 'Test Post',
                'content': 'This is a test post.'
            }), headers={'Authorization': f'Bearer {token}'},  content_type='application/json')
            self.assertEqual(response.status_code, 201)
        response = self.client.post('/api/v1/posts', data=json.dumps({
            'title': 'Test Post',
            'content': 'This is a test post.'
        }), headers={'Authorization': f'Bearer {token}'},  content_type='application/json')
        self.assertEqual(response.status_code, 429)

    def test_access_protected_endpoint_without_token(self):
        response = self.client.post('/api/v1/posts', data=json.dumps({
            'title': 'Test Post', 
            'content': 'This is a test post.'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 403)

    def test_access_protected_endpoint_with_invalid_token(self):
        response = self.client.post('/api/v1/posts', data=json.dumps({
            'title': 'Test Post',
            'content': 'This is a test post.'
        }), headers={'Authorization': 'Bearer InvalidToken'}, content_type='application/json')
        self.assertEqual(response.status_code, 403)

    def test_access_protected_endpoint_with_expired_token(self):
        # Generate an expired token for testing
        expired_token = jwt.encode({'username': 'testuser', 'exp': datetime.datetime.utcnow() - datetime.timedelta(seconds=1)}, app.config['SECRET_KEY'], algorithm='HS256')
        response = self.client.post('/api/v1/posts', data=json.dumps({
            'title': 'Test Post',
            'content': 'This is a test post.'
        }), headers={'Authorization': f'Bearer {expired_token}'}, content_type='application/json')
        self.assertEqual(response.status_code, 403)

    def test_pagination_and_sorting(self):
        self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        login_response = self.client.post('/api/login', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        token = json.loads(login_response.data)['token']
        for i in range(10):
            self.client.post('/api/v1/posts', data=json.dumps({
                'title': f'Test Post {i}',
                'content': f'This is test post {i}.'
            }), headers={'Authorization': f'Bearer {token}'}, content_type='application/json')
        response = self.client.get('/api/v1/posts?page=1&per_page=5&sort=title&direction=asc')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data['posts']), 5)

    def test_invalid_pagination_parameters(self):
        response = self.client.get('/api/v1/posts?page=0&per_page=0')
        self.assertEqual(response.status_code, 400)

    def test_invalid_sort_direction(self):
        response = self.client.get('/api/v1/posts?sort=title&direction=invalid')
        self.assertEqual(response.status_code, 400)

    def test_invalid_sort_field(self):
        response = self.client.get('/api/v1/posts?sort=invalid')
        self.assertEqual(response.status_code, 400)

    def test_search_post(self):
        self.client.post('/api/register', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        login_response = self.client.post('/api/login', data=json.dumps({
            'username': 'testuser',
            'password': 'testpassword'
        }), content_type='application/json')
        token = json.loads(login_response.data)['token']
        self.client.post('/api/v1/posts', data=json.dumps({
            'title': 'Searchable Post',
            'content': 'This post should be found by search.'
        }), headers={'Authorization': f'Bearer {token}'}, content_type='application/json')
        response = self.client.get('/api/v1/posts/search?query=Searchable')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(any(post['title'] == 'Searchable Post' for post in data))

if __name__ == '__main__':
    unittest.main()
