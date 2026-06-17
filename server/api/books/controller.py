from typing import TYPE_CHECKING, Any

from flask.views import MethodView
from flask_smorest import Blueprint

from server.api.books import service
from server.api.books.models import Livro, LivroSchema

if TYPE_CHECKING:
    from sqlalchemy import Sequence


bp = Blueprint(
    "books",
    __name__,
    url_prefix="/api/livros",
    description="Operações sobre livros",
)


@bp.route("/")
class BookController(MethodView):
    @bp.response(200, LivroSchema(many=True))
    def get(self) -> Sequence[Livro]:
        """Lista todos os livros do sistema."""
        return service.find_all()

    @bp.arguments(LivroSchema)
    @bp.response(201, LivroSchema)
    def post(self, book: dict[str, Any]) -> Livro:
        """Insere um novo livro no sistema.

        O issn pode ser fornecido em branco. Se fornecido, ele não pode conter duplicações.
        """
        return service.insert(Livro(**book))
