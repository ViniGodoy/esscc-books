from typing import TYPE_CHECKING

import pytest

from server import create_app
from server.api.books.models import LivroSchema

if TYPE_CHECKING:
    from flask import Flask


@pytest.fixture
def app() -> Flask:
    return create_app({"TESTING": True})


@pytest.fixture
def client(app: Flask):
    return app.test_client()


def test_get_books_returns(client):
    """Certificamos que o nome do autor e o link para o swagger estão lá."""
    response = client.get("/api/livros/")
    assert response.status_code == 200

    assert LivroSchema().validate(response.json)


def test_post_books(client):
    response = client.post("/api/livros/", json={"titulo": "O senhor dos aneis"})
    assert response.status_code == 422
