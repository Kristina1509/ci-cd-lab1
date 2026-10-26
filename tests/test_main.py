from fastapi.testclient import TestClient
from app.main import app, books
import app.main as main

client = TestClient(app)


def setup_function():
    books.clear()
    main.next_id = 1



def test_get_empty_list():
    response = client.get("/api/items")

    assert response.status_code == 200
    assert response.json() == []


def test_create_book():
    response = client.post(
        "/api/items",
        json={
            "title": "1984",
            "author": "George Orwell",
            "year": 1949,
        },
    )

    assert response.status_code == 201
    assert response.json()["title"] == "1984"
    assert response.json()["id"] == 1


def test_get_book():
    client.post(
        "/api/items",
        json={
            "title": "1984",
            "author": "George Orwell",
            "year": 1949,
        },
    )

    response = client.get("/api/items/1")

    assert response.status_code == 200
    assert response.json()["author"] == "George Orwell"


def test_update_book():
    client.post(
        "/api/items",
        json={
            "title": "1984",
            "author": "George Orwell",
            "year": 1949,
        },
    )

    response = client.put(
        "/api/items/1",
        json={
            "title": "Animal Farm",
            "author": "George Orwell",
            "year": 1945,
        },
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Animal Farm"


def test_delete_book():
    client.post(
        "/api/items",
        json={
            "title": "1984",
            "author": "George Orwell",
            "year": 1949,
        },
    )

    response = client.delete("/api/items/1")

    assert response.status_code == 204
    assert client.get("/api/items/1").status_code == 404


def test_missing_book():
    response = client.get("/api/items/999")

    assert response.status_code == 404
