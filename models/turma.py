class Turma:
    def __init__(self, id, descricao, professor_id, ativo):
        self.id = id
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo

    def to_dict(self):
        return self.__dict__
