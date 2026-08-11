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


@bp.route("/livros/<int:id>/editar", methods=["GET", "POST"])
def editar_livro(id):
    livro = db.get_or_404(Livro, id)

    if request.method == "POST":
        livro.titulo = request.form["titulo"]
        livro.autor = request.form["autor"]
        livro.genero = request.form["genero"]
        livro.descricao = request.form.get("descricao")

        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("editar.html", livro=livro)


@bp.route("/livros/<int:id>/excluir", methods=["POST"])
def excluir_livro(id):
    livro = db.get_or_404(Livro, id)

    db.session.delete(livro)
    db.session.commit()

    return redirect(url_for("main.index"))