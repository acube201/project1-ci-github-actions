# tests/test_app.py
from app.app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "CI with GitHub Actions works!"
