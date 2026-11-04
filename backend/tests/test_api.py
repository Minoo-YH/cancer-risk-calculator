
import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_calculate(client):
    response = client.post("/api/calculate", json={
        "age": 45,
        "smoking": "former",
        "family_history": True
    })
    assert response.status_code == 200
    assert response.json["demo_score"] == 45


def test_invalid_age(client):
    response = client.post("/api/calculate", json={
        "age": -5,
        "smoking": "never",
        "family_history": False
    })
    assert response.status_code == 400
