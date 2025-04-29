from config import db
from models.turma import Turma

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)

    def __init__(self, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre):
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre

    @property
    def media_final(self):
        return (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "turma_id": self.turma_id,
            "data_nascimento": self.data_nascimento,
            "nota_primeiro_semestre": self.nota_primeiro_semestre,
            "nota_segundo_semestre": self.nota_segundo_semestre,
            "media_final": self.media_final
        }

    @staticmethod
    def criar(data):
        campos = ['nome', 'idade', 'turma_id', 'data_nascimento', 'nota_primeiro_semestre', 'nota_segundo_semestre']
        for campo in campos:
            if campo not in data:
                return {"erro": f"Campo obrigatório ausente: {campo}"}, 400

        if not Turma.query.get(data['turma_id']):
            return {"erro": "Turma não encontrada"}, 400

        aluno = Aluno(**data)
        db.session.add(aluno)
        db.session.commit()
        return aluno.to_dict(), 201

    @staticmethod
    def listar():
        return [a.to_dict() for a in Aluno.query.all()]

    @staticmethod
    def deletar(id):
        aluno = Aluno.query.get(id)
        if not aluno:
            return {"erro": "Aluno não encontrado"}, 404
        db.session.delete(aluno)
        db.session.commit()
        return {"mensagem": "Aluno removido com sucesso"}, 200