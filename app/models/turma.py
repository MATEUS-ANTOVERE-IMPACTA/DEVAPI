class Turma:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, nome_aluno):
        self.alunos = [aluno for aluno in self.alunos if aluno.nome != nome_aluno]

