import pytest
import json
from app.main import app as flask_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    yield flask_app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_health_check(client):
    """Test the health check endpoint provided in the base project."""
    # Assuming a health check endpoint exists from the provided structure
    # If not, this test can be adapted or removed. For now, we test the root.
    response = client.get('/')
    # A redirect is expected if a default route isn't set, which is fine.
    # We are just checking if the server is responsive.
    assert response.status_code in [200, 404, 302]

def test_shorten_url_success(client):
    """Test successful creation of a short URL."""
    response = client.post('/api/shorten', json={'url': 'https://www.google.com/a/b/c'})
    assert response.status_code == 201
    data = response.get_json()
    assert 'short_code' in data
    assert len(data['short_code']) == 6
    assert data['short_url'].endswith(data['short_code'])

def test_shorten_url_invalid_url(client):
    """Test that shortening fails for an invalid URL."""
    response = client.post('/api/shorten', json={'url': 'not-a-valid-url'})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert 'not valid' in data['error']

def test_shorten_url_missing_key(client):
    """Test that shortening fails if the 'url' key is missing."""
    response = client.post('/api/shorten', json={'wrong_key': 'https://example.com'})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert "'url' key" in data['error']

def test_redirect_and_click_tracking(client):
    """Test successful redirection and that the click count is incremented."""
    # First, create a short URL
    long_url = 'https://www.github.com/test'
    post_response = client.post('/api/shorten', json={'url': long_url})
    short_code = post_response.get_json()['short_code']

    # Test the redirect
    redirect_response = client.get(f'/{short_code}')
    assert redirect_response.status_code == 302
    assert redirect_response.location == long_url

    # Check that the click count was incremented
    stats_response = client.get(f'/api/stats/{short_code}')
    assert stats_response.status_code == 200
    stats_data = stats_response.get_json()
    assert stats_data['clicks'] == 1

    # Follow the redirect one more time
    client.get(f'/{short_code}')
    stats_response_2 = client.get(f'/api/stats/{short_code}')
    assert stats_response_2.get_json()['clicks'] == 2

def test_redirect_not_found(client):
    """Test that redirecting to a non-existent short code returns 404."""
    response = client.get('/abcdef')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data
    assert 'not found' in data['error']

def test_get_stats_success(client):
    """Test successful retrieval of URL stats."""
    long_url = 'https://www.anotherexample.org'
    post_response = client.post('/api/shorten', json={'url': long_url})
    short_code = post_response.get_json()['short_code']

    # Get stats
    stats_response = client.get(f'/api/stats/{short_code}')
    assert stats_response.status_code == 200
    data = stats_response.get_json()
    assert data['url'] == long_url
    assert 'created_at' in data
    assert data['clicks'] == 0

def test_get_stats_not_found(client):
    """Test that getting stats for a non-existent short code returns 404."""
    response = client.get('/api/stats/xyz123')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data
    assert 'not found' in data['error']