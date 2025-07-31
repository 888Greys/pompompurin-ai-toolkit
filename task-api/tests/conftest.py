import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import get_db, Base

# Create test database
SQLITE_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLITE_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def test_user():
    return {
        "email": "test@example.com",
        "password": "testpassword123"
    }

@pytest.fixture
def authenticated_client(client, test_user):
    # Register user
    client.post("/auth/register", json=test_user)
    
    # Login and get token
    response = client.post(
        "/auth/login",
        data={"username": test_user["email"], "password": test_user["password"]}
    )
    token = response.json()["access_token"]
    
    # Return client with auth headers
    client.headers.update({"Authorization": f"Bearer {token}"})
    return client