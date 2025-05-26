import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.infrastructure.database import Base, engine, SessionLocal
from app.infrastructure.database import CharacterDB


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Antes de cada test: crear base en memoria limpia
    Base.metadata.create_all(bind=engine)
    yield
    # Después de cada test: eliminar todas las tablas
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)


def test_get_all_empty(client):
    response = client.get("/character/getAll")
    assert response.status_code == 200
    assert response.json() == []


def test_add_character(client):
    character = {
        "id": 1,
        "name": "Luke Skywalker",
        "height": 172,
        "mass": 77,
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": 1998
    }
    response = client.post("/character/add", json=character)
    assert response.status_code == 200
    assert response.json()["name"] == "Luke Skywalker"

    # Confirmar que se puede recuperar
    get_response = client.get("/character/get/1")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == 1


def test_add_duplicate_character(client):
    character = {
        "id": 2,
        "name": "Darth Vader",
        "height": 202,
        "mass": 136,
        "hair_color": "none",
        "skin_color": "white",
        "eye_color": "yellow",
        "birth_year": 1977
    }
    client.post("/character/add", json=character)
    duplicate = client.post("/character/add", json=character)
    assert duplicate.status_code == 400
    assert "already exists" in duplicate.json()["detail"]


def test_delete_character(client):
    character = {
        "id": 3,
        "name": "Leia Organa",
        "height": 150,
        "mass": 49,
        "hair_color": "brown",
        "skin_color": "light",
        "eye_color": "brown",
        "birth_year": 1998
    }
    client.post("/character/add", json=character)

    delete_response = client.delete("/character/delete/3")
    assert delete_response.status_code == 200
    assert "deleted" in delete_response.json()["detail"]

    # Confirmar que ya no existe
    get_response = client.get("/character/get/3")
    assert get_response.status_code == 404


def test_delete_nonexistent_character(client):
    response = client.delete("/character/delete/999")
    assert response.status_code == 400
    assert "not found" in response.json()["detail"]
