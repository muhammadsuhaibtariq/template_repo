import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_main_route(client):
    """Test the main route '/' returns 'Welcome!'"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Welcome to Flask!!!'

def test_how_are_you_route(client):
    """Test the '/how are you' route returns the correct message"""
    response = client.get('/how are you')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'I am good, how about you ?'

def test_nonexistent_route(client):
    """Test that accessing a non-existent route returns 404"""
    response = client.get('/nonexistent')
    assert response.status_code == 404