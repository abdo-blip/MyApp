import sys
import os
import pytest


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from App import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_add_product(client):
    response = client.post('/add_product', json={"name": "Laptop", "quantity": 5})
    assert response.status_code == 201
    assert b"Product added successfully!" in response.data
    
    
def test_delete_product(client):
    response = client.post('/delete_product', json={"name": "Laptop", "quantity": 3})
    assert response.status_code == 202
    assert b"Product deleted successfully!" in response.data