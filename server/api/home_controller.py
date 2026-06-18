from flask import Blueprint, Response, redirect, render_template

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def index() -> str:
    return render_template("index.html")


@bp.route("/api")
def api_redirect() -> Response:
    return redirect("/api/swagger-ui")
