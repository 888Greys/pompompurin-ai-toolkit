import pytest
from fastapi.testclient import TestClient

def test_register_user(client: TestClient):
    response = client.post(
        "/auth/register",
        json={"email": "newuser@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "newuser@example.com"
    assert "id" in data

def test_register_duplicate_email(client: TestClient):
    user_data = {"email": "duplicate@example.com", "password": "password123"}
    
    # Register first time
    response = client.post("/auth/register", json=user_data)
    assert response.status_code == 200
    
    # Try to register again
    response = client.post("/auth/register", json=user_data)
    assert response.status_code == 400
    assert "Email already registered" in response.json()["detail"]

def test_login_user(client: TestClient, test_user):
    # Register user first
    client.post("/auth/register", json=test_user)
    
    # Login
    response = client.post(
        "/auth/login",
        data={"username": test_user["email"], "password": test_user["password"]}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_credentials(client: TestClient):
    response = client.post(
        "/auth/login",
        data={"username": "nonexistent@example.com", "password": "wrongpassword"}
    )
    assert response.status_code == 401
    assert "Incorrect email or password" in response.json()["detail"]