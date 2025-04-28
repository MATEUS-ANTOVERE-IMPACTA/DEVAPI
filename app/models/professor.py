from config import db

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    def __init__(self, nome):
        self.nome = nome

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }