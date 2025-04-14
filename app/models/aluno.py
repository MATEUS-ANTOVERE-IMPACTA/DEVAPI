class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = self.calcular_media()

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def atualizar_notas(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = self.calcular_media()
