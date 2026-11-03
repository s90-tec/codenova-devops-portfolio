from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home_returns_welcome_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the CodeNova DevOps Demo API",
        "docs": "/docs",
        "health": "/health",
    }


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_greet_endpoint():
    response = client.get("/greet/Shubham")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, Shubham! Welcome to CodeNova DevOps."
    }


def test_about_endpoint():
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json() == {
        "project": "CodeNova DevOps Portfolio",
        "purpose": "DevOps Internship Demonstration",
    }


def test_unknown_endpoint_returns_not_found():
    response = client.get("/does-not-exist")
    assert response.status_code == 404
