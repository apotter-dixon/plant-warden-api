from json.tool import main
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/plants")
    assert response.status_code == 200
    assert response.json() == [{"name": "flower"}, {"name": "grass"}]