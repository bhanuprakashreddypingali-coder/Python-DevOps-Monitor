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

    assert "text/plain" in response.headers["content-type"]

    metrics = response.text

    assert "app_requests_total" in metrics
    assert "system_cpu_usage_percent" in metrics
    assert "system_memory_usage_percent" in metrics
    assert "system_disk_usage_percent" in metrics