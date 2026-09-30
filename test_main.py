from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "UP"


def test_metrics():
    response = client.get("/metrics")

    assert response.status_code == 200

    data = response.json()

    assert "cpu_percent" in data
    assert "memory" in data
    assert "disk" in data