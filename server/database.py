from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Instancia as extensões no escopo global
db = SQLAlchemy(model_class=Base)
migrate = Migrate()
