# tests/test_api.py
import json
from project.models import User

def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"User Management System is running" in response.data

def test_create_user(client):
    """Test user creation."""
    response = client.post('/users', data=json.dumps({
        "name": "Test User",
        "email": "test@example.com",
        "password": "password123"
    }), content_type='application/json')
    assert response.status_code == 201
    assert b"test@example.com" in response.data

def test_login(client):
    """Test user login and JWT token generation."""
    # First, create a user to log in with
    client.post('/users', data=json.dumps({
        "name": "Login User",
        "email": "login@example.com",
        "password": "password123"
    }), content_type='application/json')

    # Now, attempt to log in
    response = client.post('/login', data=json.dumps({
        "email": "login@example.com",
        "password": "password123"
    }), content_type='application/json')
    assert response.status_code == 200
    json_data = response.get_json()
    assert "access_token" in json_data

def test_get_all_users(client):
    """Test retrieving all users."""
    response = client.get('/users')
    assert response.status_code == 200
    json_data = response.get_json()
    assert isinstance(json_data, list)

def test_get_specific_user(client):
    """Test retrieving a single user by ID."""
    # Create a user first
    res = client.post('/users', data=json.dumps({
        "name": "Specific User", "email": "specific@example.com", "password": "abc"
    }), content_type='application/json')
    user_id = res.get_json()['id']
    
    response = client.get(f'/user/{user_id}')
    assert response.status_code == 200
    assert b"Specific User" in response.data

def test_update_user(client):
    """Test updating a user's information."""
    res = client.post('/users', data=json.dumps({
        "name": "Update Me", "email": "update@example.com", "password": "abc"
    }), content_type='application/json')
    user_id = res.get_json()['id']

    response = client.put(f'/user/{user_id}', data=json.dumps({
        "name": "Updated Name"
    }), content_type='application/json')
    assert response.status_code == 200
    assert b"Updated Name" in response.data

def test_delete_user(client):
    """Test deleting a user."""
    res = client.post('/users', data=json.dumps({
        "name": "Delete Me", "email": "delete@example.com", "password": "abc"
    }), content_type='application/json')
    user_id = res.get_json()['id']
    
    response = client.delete(f'/user/{user_id}')
    assert response.status_code == 204

    # Verify user is deleted
    get_response = client.get(f'/user/{user_id}')
    assert get_response.status_code == 404

def test_search_user(client):
    """Test searching for a user by name."""
    client.post('/users', data=json.dumps({
        "name": "Searchable Guy", "email": "search@example.com", "password": "abc"
    }), content_type='application/json')
    
    response = client.get('/search?name=Searchable')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) > 0
    assert json_data[0]['name'] == "Searchable Guy"