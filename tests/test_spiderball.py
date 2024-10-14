import subprocess
import time
import requests

def start_test_server():
    # Start the Flask test server
    server = subprocess.Popen(['python', 'tests/test_server.py'])
    time.sleep(2)  # Wait for the server to start
    return server

def stop_test_server(server):
    # Terminate the Flask test server
    server.terminate()

def test_login():
    server = start_test_server()
    try:
        # Test login functionality
        response = requests.post('http://localhost:5000/login', data={'username': 'testuser', 'password': 'password'})
        assert response.status_code == 200
        assert 'Hello, testuser!' in response.text
    finally:
        stop_test_server(server)

def test_protected_access():
    server = start_test_server()
    try:
        # Test access to protected page without login
        response = requests.get('http://localhost:5000/protected')
        assert response.status_code == 401
    finally:
        stop_test_server(server)

def test_404_handling():
    server = start_test_server()
    try:
        # Test handling of 404 page
        response = requests.get('http://localhost:5000/404')
        assert response.status_code == 404
    finally:
        stop_test_server(server)

# Additional tests can be added here for expired sessions, invalid passwords, etc.
