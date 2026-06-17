import datetime

from marshmallow import Schema, ValidationError, fields, validate
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from server.database import db

# Database models

class Livro(db.Model):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(255), nullable=False)
    autor: Mapped[str] = mapped_column(String(255), nullable=False)
    issn: Mapped[str] = mapped_column(String(9), nullable=False, default="")
    data_publicacao = mapped_column(DateTime(), nullable=False)
    paginas: Mapped[int] = mapped_column(nullable=False, default=0)

# Request and response models

def is_in_the_past(date: datetime.datetime) -> None:
    if date > datetime.datetime.now(tz=datetime.UTC):
        raise ValidationError("A data deve estar no passado.")
    

class LivroSchema(Schema):
    id = fields.Int(dump_only=True)
    titulo = fields.Str(
        required=True,
        validate=validate.Length(
            min=1,
            max=255,
            error="O campo 'titulo' é obrigatório e não pode estar em branco.",
        ),
    )
    autor = fields.Str(
        required=True,
        validate=validate.Length(
            min=1,
            max=255,
            error="O campo 'autor' é obrigatório e não pode estar em branco.",
        ),
    )
    issn = fields.Str(
        required=True,
        validate=validate.Regexp(
            r"^(?:[0-9]{4}-[0-9]{4})?$",
            error="O 'issn' deve estar no formato XXXX-XXXX.",
        ),
    )
    data_publicacao = fields.AwareDateTime(
        required=True, 
        format="%Y-%m-%d",
        default_timezone=datetime.UTC, 
        validate=is_in_the_past
    )
    paginas = fields.Int(
        required=True,
        validate=validate.Range(
            min=0,
            max=100000,
            error="O número de 'paginas' deve ser positivo.",
        ),
    )

    class Meta:
        ordered = True
