from flask import Blueprint, render_template

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def index() -> str:
    return render_template("index.html")
