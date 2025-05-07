from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

<<<<<<< HEAD
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Vibe Coding Test API"}

def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
=======
def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
>>>>>>> 71d6162cc6dd729ffe2e29683176600597ce7151
