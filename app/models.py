from . import db


class Livro(db.Model):
    __tablename__ = "livros"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(150), nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Livro {self.titulo}>"