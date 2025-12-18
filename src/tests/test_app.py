from fastapi.testclient import TestClient
from retail_shop.app import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}
