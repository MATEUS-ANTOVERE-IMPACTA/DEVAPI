from config import db

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    def __init__(self, nome):
        self.nome = nome

    def to_dict(self):
        return {"id": self.id, "nome": self.nome}

    @staticmethod
    def criar(data):
        if "nome" not in data:
            return {"erro": "Campo nome é obrigatório"}, 400
        prof = Professor(nome=data["nome"])
        db.session.add(prof)
        db.session.commit()
        return prof.to_dict(), 201

    @staticmethod
    def listar():
        return [p.to_dict() for p in Professor.query.all()]

    @staticmethod
    def deletar(id):
        prof = Professor.query.get(id)
        if not prof:
            return {"erro": "Professor não encontrado"}, 404
        db.session.delete(prof)
        db.session.commit()
        return {"mensagem": "Professor removido"}, 200