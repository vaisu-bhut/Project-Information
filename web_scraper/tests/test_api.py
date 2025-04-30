# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_scrape_endpoint():
    response = client.post("/scrape", json={"url": "https://example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert "headings" in data
    assert "paragraphs" in data
    assert "links" in data