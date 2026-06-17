from pathlib import Path
from typing import TYPE_CHECKING, Any

from flask import Flask
from flask_smorest import Api

from server.database import db  # Importa o objeto db

if TYPE_CHECKING:
    from collections.abc import Mapping


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.json.ensure_ascii = False
    app.json.sort_keys = False
    instance_path = Path(app.instance_path or ".")

    # Configurações da API movidas para o prefixo /api
    app.config["API_TITLE"] = "Servidor de Livros API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/api"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    # Configuração do SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///livros.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    instance_path.mkdir(parents=True, exist_ok=True)

    # Inicializa o SQLAlchemy com o aplicativo Flask
    db.init_app(app)

    # Cria as tabelas do banco de dados dentro do contexto da aplicação
    with app.app_context():
        from server.api.books.models import Livro  # noqa: F401

        db.create_all()

    # Inicializa o flask-smorest
    api = Api(app)

    # Registra o blueprint da página inicial (home)
    from server.api.home_controller import bp as home_bp

    app.register_blueprint(home_bp)

    # Registra os blueprints da API
    from server.api.books.controller import bp as books_bp

    api.register_blueprint(books_bp)

    return app
