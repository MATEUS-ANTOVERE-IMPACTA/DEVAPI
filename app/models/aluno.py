from config import db

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