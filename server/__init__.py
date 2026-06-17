from pathlib import Path
from typing import TYPE_CHECKING, Any

from flask import Flask
from flask_smorest import Api

from server.api.book_controller import api_bp
from server.root_controller import home_bp

if TYPE_CHECKING:
    from collections.abc import Mapping


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.json.ensure_ascii = False
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

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    instance_path.mkdir(parents=True, exist_ok=True)

    # Inicializa o flask-smorest
    api = Api(app)

    # Registra o blueprint da página inicial (home)
    app.register_blueprint(home_bp)

    # Registra o blueprint da API no objeto Api do flask-smorest
    api.register_blueprint(api_bp)

    return app
