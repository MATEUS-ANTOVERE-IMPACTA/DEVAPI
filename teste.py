import requests

BASE_URL = "http://127.0.0.1:5000"

def testar_reset():
    r = requests.post(f"{BASE_URL}/reseta")
    try:
        print("RESET:", r.status_code, r.json())
    except requests.exceptions.JSONDecodeError:
        print("RESET:", r.status_code, "Resposta não é JSON:", r.text)

def testar_post_professor():
    professor = {
        "nome": "Maria Oliveira"
    }
    r = requests.post(f"{BASE_URL}/professores", json=professor)
    print("POST /professores:", r.status_code, r.json())
    return r.json().get("id")

def testar_post_turma(professor_id):
    turma = {
        "descricao": "Turma A",
        "professor_id": professor_id,
        "ativo": True
    }
    r = requests.post(f"{BASE_URL}/turmas", json=turma)
    print("POST /turmas:", r.status_code, r.json())
    return r.json().get("id")

def testar_post_aluno(turma_id):
    aluno = {
        "nome": "João da Silva",
        "idade": 20,
        "turma_id": turma_id,
        "data_nascimento": "2003-05-15",
        "nota_primeiro_semestre": 7.5,
        "nota_segundo_semestre": 8.0
    }
    r = requests.post(f"{BASE_URL}/alunos", json=aluno)
    print("POST /alunos:", r.status_code, r.json())

def testar_gets():
    print("\nGET /professores:", requests.get(f"{BASE_URL}/professores").json())
    print("GET /turmas:", requests.get(f"{BASE_URL}/turmas").json())
    print("GET /alunos:", requests.get(f"{BASE_URL}/alunos").json())

if __name__ == "__main__":
    testar_reset()

    professor_id = testar_post_professor()
    turma_id = testar_post_turma(professor_id)
    testar_post_aluno(turma_id)

    testar_gets()