from flask.views import MethodView
from flask_smorest import Blueprint

api_bp = Blueprint(
    "api", __name__, description="Operações da API do Servidor de Livros"
)


@api_bp.route("/livros")
class BookController(MethodView):
    @api_bp.doc(
        summary="Lista todos os livros disponíveis",
        description="Lista os livros cadastrados.",
    )
    def get(self) -> dict[str, str]:
        return {}
