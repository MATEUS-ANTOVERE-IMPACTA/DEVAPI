import requests

BASE_URL = "http://127.0.0.1:5000"

def testar_reset():
    r = requests.post(f"{BASE_URL}/reseta")
    print("RESET:", r.status_code, r.json())

def testar_post_professor(nome):
    r = requests.post(f"{BASE_URL}/professores", json={"nome": nome})
    print(f"POST /professores: {nome} =>", r.status_code, r.json())
    return r.json().get("id")

def testar_post_turma(descricao, professor_id):
    r = requests.post(f"{BASE_URL}/turmas", json={
        "descricao": descricao,
        "professor_id": professor_id,
        "ativo": True
    })
    print(f"POST /turmas: {descricao} =>", r.status_code, r.json())
    return r.json().get("id")

def testar_post_aluno(nome, idade, turma_id):
    r = requests.post(f"{BASE_URL}/alunos", json={
        "nome": nome,
        "idade": idade,
        "turma_id": turma_id,
        "data_nascimento": "2003-01-01",
        "nota_primeiro_semestre": 8.0,
        "nota_segundo_semestre": 9.0
    })
    print(f"POST /alunos: {nome} =>", r.status_code, r.json())
    return r.json().get("id")

def testar_get(endpoint):
    r = requests.get(f"{BASE_URL}/{endpoint}")
    print(f"GET /{endpoint} =>", r.status_code, r.json())

def testar_put_aluno(id):
    r = requests.put(f"{BASE_URL}/alunos/{id}", json={
        "nome": "Aluno Atualizado",
        "idade": 21,
        "turma_id": 1,
        "data_nascimento": "2000-01-01",
        "nota_primeiro_semestre": 10,
        "nota_segundo_semestre": 10
    })
    print(f"PUT /alunos/{id} =>", r.status_code, r.json())

def testar_put_professor(id):
    r = requests.put(f"{BASE_URL}/professores/{id}", json={"nome": "Professor Atualizado"})
    print(f"PUT /professores/{id} =>", r.status_code, r.json())

def testar_put_turma(id):
    r = requests.put(f"{BASE_URL}/turmas/{id}", json={
        "descricao": "Turma Atualizada",
        "professor_id": 1,
        "ativo": False
    })
    print(f"PUT /turmas/{id} =>", r.status_code, r.json())

def testar_delete(endpoint, id):
    r = requests.delete(f"{BASE_URL}/{endpoint}/{id}")
    print(f"DELETE /{endpoint}/{id} =>", r.status_code, r.json())

def testar_delete_inexistente(endpoint, id):
    r = requests.delete(f"{BASE_URL}/{endpoint}/{id}")
    print(f"DELETE /{endpoint}/{id} (inexistente) =>", r.status_code, r.json())

def testar_post_aluno_invalido():
    r = requests.post(f"{BASE_URL}/alunos", json={"nome": "Sem idade"})
    print("POST /alunos (inválido) =>", r.status_code, r.json())

# Execução dos testes
if __name__ == "__main__":
    testar_reset()  # Teste 1

    # Professores
    id_prof1 = testar_post_professor("Maria")            # Teste 2
    id_prof2 = testar_post_professor("João")             # Teste 3
    testar_get("professores")                            # Teste 4

    # Turmas
    id_turma1 = testar_post_turma("Turma A", id_prof1)   # Teste 5
    id_turma2 = testar_post_turma("Turma B", id_prof2)   # Teste 6
    testar_get("turmas")                                 # Teste 7

    # Alunos
    id_aluno1 = testar_post_aluno("Ana", 20, id_turma1)  # Teste 8
    id_aluno2 = testar_post_aluno("Carlos", 22, id_turma2) # Teste 9
    testar_get("alunos")                                 # Teste 10

    # PUTs
    testar_put_aluno(id_aluno1)                          # Teste 11
    testar_put_professor(id_prof1)                       # Teste 12
    testar_put_turma(id_turma1)                          # Teste 13

    # DELETEs
    testar_delete("alunos", id_aluno2)                   # Teste 14
    testar_delete("professores", id_prof2)               # Teste 15
    testar_delete("turmas", id_turma2)                   # Teste 16

    # Erros
    testar_delete_inexistente("alunos", 999)             # Teste 17
    testar_post_aluno_invalido()                         # Teste 18