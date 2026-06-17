import logging
from typing import TYPE_CHECKING

from sqlalchemy.exc import SQLAlchemyError

from server.api.books.models import Livro
from server.database import db

if TYPE_CHECKING:
    from collections.abc import Sequence

logger = logging.getLogger(__name__)


def find_all() -> Sequence[Livro]:
    try:
        return db.session.scalars(db.select(Livro)).all()
    except SQLAlchemyError as error:
        logger.exception(msg="Erro ao listar livros do banco de dados.", exc_info=error)
        return []


def find_by_issn(issn: str) -> Livro | None:
    stmt = db.select(Livro).filter_by(issn=issn)
    return db.session.execute(stmt).scalar_one_or_none()


def save(book: Livro) -> Livro:
    try:
        db.session.add(book)
        db.session.commit()
    except SQLAlchemyError as error:
        db.session.rollback()
        logger.exception(
            msg="Erro ao salvar o livro '%(title)s' no banco de dados.",
            extra={"title": book.titulo},
            exc_info=error,
        )
        raise
    else:
        return book
