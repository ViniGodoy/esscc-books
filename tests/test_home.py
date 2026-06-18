from typing import TYPE_CHECKING

import pytest

from server import create_app

if TYPE_CHECKING:
    from flask import Flask


@pytest.fixture
def app() -> Flask:
    return create_app({"TESTING": True})


@pytest.fixture
def client(app: Flask):
    return app.test_client()


def test_index_page_contains_author(client):
    """Certificamos que o nome do autor e o link para o swagger estão lá."""
    response = client.get("/")
    body = response.text
    assert response.status_code == 200
    assert "/api/swagger-ui" in body
    assert "Vinícius G. Mendonça" in body


def test_swagger_page_opens(client):
    response = client.get("/api/swagger-ui")
    assert response.status_code == 200
    assert "Servidor de Livros API" in response.text


def test_api_redirects_to_swagger(client):
    response = client.get("/api", follow_redirects=False)
    assert response.status_code in (301, 302, 303, 307, 308)
    assert response.headers["Location"] == "/api/swagger-ui"
