from collections.abc import Mapping
from pathlib import Path
from typing import Any

from flask import Flask, Response, jsonify


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.json.ensure_ascii = False
    instance_path = Path(app.instance_path or ".")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    instance_path.mkdir(parents=True, exist_ok=True)

    # a simple page that says hello
    @app.route("/")
    def hello() -> Response:
        return jsonify({"Aluno": "Vinícius Godoy de Mendonça"})

    return app
