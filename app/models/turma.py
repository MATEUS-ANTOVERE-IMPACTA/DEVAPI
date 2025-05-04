from config import db
from models.professor import Professor

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    def __init__(self, descricao, professor_id, ativo=True):
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo

    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "professor_id": self.professor_id,
            "ativo": self.ativo
        }

    @staticmethod
    def criar(data):
        if 'descricao' not in data or 'professor_id' not in data:
            return {"erro": "Campos obrigatórios ausentes"}, 400
        if not Professor.query.get(data['professor_id']):
            return {"erro": "Professor não encontrado"}, 400
        turma = Turma(**data)
        db.session.add(turma)
        db.session.commit()
        return turma.to_dict(), 201

    @staticmethod
    def listar():
        return [t.to_dict() for t in Turma.query.all()]

    @staticmethod
    def deletar(id):
        turma = Turma.query.get(id)
        if not turma:
            return {"erro": "Turma não encontrada"}, 404
        db.session.delete(turma)
        db.session.commit()
        return {"mensagem": "Turma removida"}, 200

    @staticmethod
    def atualizar(id, data):
        turma = Turma.query.get(id)
        if not turma:
            return {"erro": "Turma não encontrada"}, 404
        if 'descricao' not in data or 'professor_id' not in data:
            return {"erro": "Campos obrigatórios ausentes"}, 400
        if not Professor.query.get(data['professor_id']):
            return {"erro": "Professor não encontrado"}, 400
        turma.descricao = data['descricao']
        turma.professor_id = data['professor_id']
        turma.ativo = data.get('ativo', turma.ativo)
        db.session.commit()
        return turma.to_dict(), 200