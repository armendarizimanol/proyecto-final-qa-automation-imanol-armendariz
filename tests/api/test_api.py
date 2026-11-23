
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_obtener_publicacion():

    response = requests.get(
        f"{BASE_URL}/posts/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert "title" in data
    assert "body" in data


def test_crear_publicacion():

    nueva_publicacion = {
        "title": "Prueba de automatizacion",
        "body": "Contenido de prueba QA",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=nueva_publicacion
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == nueva_publicacion["title"]
    assert data["body"] == nueva_publicacion["body"]
    assert data["userId"] == nueva_publicacion["userId"]
    assert "id" in data


def test_eliminar_publicacion():

    response = requests.delete(
        f"{BASE_URL}/posts/1"
    )

    assert response.status_code == 200
