from typing import TYPE_CHECKING

from flask_smorest import abort

from server.api.books import repository

if TYPE_CHECKING:
    from collections.abc import Sequence

    from server.api.books.models import Livro


def find_all() -> Sequence[Livro]:
    return repository.find_all()


def insert(book: Livro) -> Livro:
    if book.issn and repository.find_by_issn(book.issn):
        abort(422, message=f"O issn '{book.issn}' já está cadastrado.")

    return repository.save(book)
