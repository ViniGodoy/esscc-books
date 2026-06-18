import datetime
from types import SimpleNamespace

import pytest

from server import create_app
from server.api.books import repository


def _book_body(**kwargs):
    """Retorna um payload de livro falso para uso em testes.

    Valores defaults seguem so formato esperado pelo endpoint de livros.
    Qualquer chave pode ser sobrescrita passando kwargs.
    """
    book_id = kwargs.get("id")
    book = {
        "titulo": f"Livro de Teste {book_id or 1}",
        "autor": f"Autor de Teste {book_id or 1}",
        "issn": "1234-5678",
        "data_publicacao": "2024-01-01",
        "paginas": (book_id or 1) * 100,
    }
    book.update(kwargs)
    return book


@pytest.fixture
def app():
    return create_app({"TESTING": True})


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_livros_returns_two_books(client, monkeypatch):
    books = [
        _book_body(
            id=1, data_publicacao=datetime.datetime(2026, 1, 1, tzinfo=datetime.UTC)
        ),
        _book_body(
            id=2, data_publicacao=datetime.datetime(2026, 2, 2, tzinfo=datetime.UTC)
        ),
    ]
    monkeypatch.setattr(repository, "find_all", lambda: books)

    response = client.get("/api/livros/")

    assert response.status_code == 200
    assert response.is_json
    assert response.json == [
        {
            "id": 1,
            "titulo": "Livro de Teste 1",
            "autor": "Autor de Teste 1",
            "issn": "1234-5678",
            "data_publicacao": "2026-01-01",
            "paginas": 100,
        },
        {
            "id": 2,
            "titulo": "Livro de Teste 2",
            "autor": "Autor de Teste 2",
            "issn": "1234-5678",
            "data_publicacao": "2026-02-02",
            "paginas": 200,
        },
    ]


def test_post_livros_creates_when_payload_is_valid(client, monkeypatch):
    payload = _book_body()
    captured = {}

    def fake_save(book):
        captured["book"] = book

        return SimpleNamespace(
            id=1,
            titulo=book.titulo,
            autor=book.autor,
            issn=book.issn,
            data_publicacao=book.data_publicacao,
            paginas=book.paginas,
        )

    monkeypatch.setattr(repository, "find_by_issn", lambda issn: None)
    monkeypatch.setattr(repository, "save", fake_save)

    response = client.post("/api/livros/", json=payload)

    assert response.status_code == 201
    assert response.is_json

    body = response.json
    assert body["id"] == 1
    assert body["titulo"] == payload["titulo"]
    assert body["autor"] == payload["autor"]
    assert body["issn"] == payload["issn"]
    assert body["data_publicacao"] == payload["data_publicacao"]
    assert body["paginas"] == payload["paginas"]


def test_post_livros_returns_422_when_issn_is_invalid(client):
    response = client.post("/api/livros/", json=_book_body(issn="12345678"))

    assert response.status_code == 422
    assert "issn" in response.text
    assert "XXXX-XXXX" in response.text


def test_post_livros_returns_422_when_title_is_blank(client):
    response = client.post("/api/livros/", json=_book_body(titulo=""))

    assert response.status_code == 422
    assert "titulo" in response.text
    assert "obrigatório" in response.text


def test_post_livros_returns_422_when_author_is_blank(client):
    response = client.post("/api/livros/", json=_book_body(autor=""))

    assert response.status_code == 422
    assert "autor" in response.text
    assert "obrigatório" in response.text


def test_post_livros_returns_422_when_pages_are_negative(client):
    response = client.post("/api/livros/", json=_book_body(paginas=-1))

    assert response.status_code == 422
    assert "paginas" in response.text
    assert "positivo" in response.text


def test_post_livros_returns_422_when_publication_date_is_invalid(client):
    response = client.post(
        "/api/livros/", json=_book_body(data_publicacao="2024-13-01")
    )

    assert response.status_code == 422
    assert "data_publicacao" in response.text


def test_post_livros_returns_422_when_publication_date_is_in_the_future(client):
    response = client.post(
        "/api/livros/", json=_book_body(data_publicacao="2500-01-01")
    )

    assert response.status_code == 422
    assert "data_publicacao" in response.text
    assert "passado" in response.text


@pytest.mark.parametrize(
    "field",
    ["titulo", "autor", "issn", "data_publicacao", "paginas"],
)
def test_post_livros_returns_422_when_required_field_is_missing(client, field):
    payload = _book_body()
    payload.pop(field, None)

    response = client.post("/api/livros/", json=payload)

    assert response.status_code == 422
    assert field in response.text


def test_post_livros_returns_422_when_issn_is_duplicate(client, monkeypatch):
    monkeypatch.setattr(repository, "find_by_issn", lambda issn: object())
    response = client.post("/api/livros/", json=_book_body())

    assert response.status_code == 422
    assert "já está cadastrado" in response.text
