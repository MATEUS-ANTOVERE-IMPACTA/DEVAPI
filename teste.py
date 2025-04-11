import requests

BASE_URL = "http://127.0.0.1:5000"

def testar_get_alunos():
    response = requests.get(f"{BASE_URL}/alunos")
    print("GET /alunos:", response.status_code, response.json())

def testar_post_aluno():
    novo_aluno = {
        "id": 1,
        "nome": "João da Silva",
        "idade": 20
    }
    response = requests.post(f"{BASE_URL}/alunos", json=novo_aluno)
    print("POST /alunos:", response.status_code, response.json())

def testar_get_professores():
    response = requests.get(f"{BASE_URL}/professores")
    print("GET /professores:", response.status_code, response.json())

def testar_post_professor():
    novo_professor = {
        "id": 1,
        "nome": "Maria Oliveira",
        "disciplina": "Matemática"
    }
    response = requests.post(f"{BASE_URL}/professores", json=novo_professor)
    print("POST /professores:", response.status_code, response.json())

def testar_get_turmas():
    response = requests.get(f"{BASE_URL}/turmas")
    print("GET /turmas:", response.status_code, response.json())

def testar_post_turma():
    nova_turma = {
        "id": 1,
        "nome": "Turma A",
        "alunos": [1],
        "professor_id": 1
    }
    response = requests.post(f"{BASE_URL}/turmas", json=nova_turma)
    print("POST /turmas:", response.status_code, response.json())

# Execução dos testes
if __name__ == "__main__":
    testar_get_alunos()
    testar_post_aluno()
    testar_get_alunos()

    testar_get_professores()
    testar_post_professor()
    testar_get_professores()

    testar_get_turmas()
    testar_post_turma()
    testar_get_turmas()