from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Livro

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    livros = Livro.query.all()
    return render_template("index.html", livros=livros)


@bp.route("/livros", methods=["POST"])
def criar_livro():
    livro = Livro(
        titulo=request.form["titulo"],
        autor=request.form["autor"],
        genero=request.form["genero"],
        descricao=request.form.get("descricao")
    )

    db.session.add(livro)
    db.session.commit()

    return redirect(url_for("main.index"))