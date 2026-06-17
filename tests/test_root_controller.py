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
