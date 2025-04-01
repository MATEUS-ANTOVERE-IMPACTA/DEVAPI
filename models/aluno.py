class Aluno:
    def __init__(self, id, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = self.calcular_media()

    def calcular_media(self):
        return (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2

    def to_dict(self):
        return self.__dict__
