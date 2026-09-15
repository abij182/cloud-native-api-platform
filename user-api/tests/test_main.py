from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_users():
    response = client.get("/api/users")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_user():
    response = client.get("/api/users/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1
