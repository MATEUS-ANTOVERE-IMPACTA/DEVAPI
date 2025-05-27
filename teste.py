import requests

BASE_URL = "http://127.0.0.1:5000"

def testar_reset():
    r = requests.post(f"{BASE_URL}/reseta")
    try:
        print("1. RESET:", r.status_code, r.json())
    except requests.exceptions.JSONDecodeError:
        print("1. RESET:", r.status_code, "Resposta não é JSON:", r.text)

def testar_post_professor():
    professor = {"nome": "Maria Oliveira"}
    r = requests.post(f"{BASE_URL}/professores", json=professor)
    try:
        print("2. POST /professores:", r.status_code, r.json())
        return r.json().get("id")
    except requests.exceptions.JSONDecodeError:
        print("2. POST /professores falhou:", r.status_code, r.text)
        return None

def testar_get_professores():
    r = requests.get(f"{BASE_URL}/professores")
    print("3. GET /professores:", r.status_code, r.json())

def testar_delete_professor(professor_id):
    r = requests.delete(f"{BASE_URL}/professores/{professor_id}")
    print("4. DELETE /professores:", r.status_code, r.json())

def testar_post_turma(professor_id):
    turma = {
        "descricao": "Turma A",
        "professor_id": professor_id,
        "ativo": True
    }
    r = requests.post(f"{BASE_URL}/turmas", json=turma)
    try:
        print("5. POST /turmas:", r.status_code, r.json())
        return r.json().get("id")
    except requests.exceptions.JSONDecodeError:
        print("5. POST /turmas falhou:", r.status_code, r.text)
        return None

def testar_get_turmas():
    r = requests.get(f"{BASE_URL}/turmas")
    print("6. GET /turmas:", r.status_code, r.json())

def testar_delete_turma(turma_id):
    r = requests.delete(f"{BASE_URL}/turmas/{turma_id}")
    print("7. DELETE /turmas:", r.status_code, r.json())

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
    try:
        print("8. POST /alunos:", r.status_code, r.json())
        return r.json().get("id")
    except requests.exceptions.JSONDecodeError:
        print("8. POST /alunos falhou:", r.status_code, r.text)
        return None

def testar_get_alunos():
    r = requests.get(f"{BASE_URL}/alunos")
    print("9. GET /alunos:", r.status_code, r.json())

def testar_put_aluno(aluno_id, turma_id):
    dados = {
        "nome": "João Atualizado",
        "idade": 21,
        "turma_id": turma_id,
        "data_nascimento": "2003-05-15",
        "nota_primeiro_semestre": 9.0,
        "nota_segundo_semestre": 9.5
    }
    r = requests.put(f"{BASE_URL}/alunos/{aluno_id}", json=dados)
    try:
        print("10. PUT /alunos:", r.status_code, r.json())
    except requests.exceptions.JSONDecodeError:
        print("10. PUT /alunos falhou:", r.status_code, r.text)

def testar_delete_aluno(aluno_id):
    r = requests.delete(f"{BASE_URL}/alunos/{aluno_id}")
    print("11. DELETE /alunos:", r.status_code, r.json())

def testar_put_professor(professor_id):
    r = requests.put(f"{BASE_URL}/professores/{professor_id}", json={"nome": "Nome Atualizado"})
    print("12. PUT /professores:", r.status_code, r.json())

def testar_put_turma(turma_id, professor_id):
    r = requests.put(f"{BASE_URL}/turmas/{turma_id}", json={
        "descricao": "Turma Atualizada",
        "professor_id": professor_id,
        "ativo": False
    })
    print("13. PUT /turmas:", r.status_code, r.json())

def testar_get_home():
    r = requests.get(f"{BASE_URL}/")
    print("14. GET /:", r.status_code, r.text)

def testar_get_swagger():
    r = requests.get(f"{BASE_URL}/apidocs/")
    print("15. GET /apidocs/:", r.status_code, "OK" if r.status_code == 200 else "Erro")

# NOVAS FUNÇÕES DE TESTE: ReservasAPI e AtividadesAPI
def testar_post_reserva(turma_id):
    reserva = {
        "sala": "Sala 101",
        "horario": "10:00 - 12:00",
        "turma_id": turma_id
    }
    try:
        r = requests.post("http://127.0.0.1:5001/reservas", json=reserva)
        print("16. POST /reservas:", r.status_code, r.json())
    except requests.exceptions.RequestException as e:
        print("16. POST /reservas falhou:", str(e))

def testar_get_reservas():
    try:
        r = requests.get("http://127.0.0.1:5001/reservas")
        print("17. GET /reservas:", r.status_code, r.json())
    except requests.exceptions.RequestException as e:
        print("17. GET /reservas falhou:", str(e))

def testar_post_atividade(professor_id):
    atividade = {
        "titulo": "Seminário de Segurança",
        "descricao": "Apresentação sobre firewalls",
        "professor_id": professor_id
    }
    try:
        r = requests.post("http://127.0.0.1:5002/atividades", json=atividade)
        print("18. POST /atividades:", r.status_code, r.json())
    except requests.exceptions.RequestException as e:
        print("18. POST /atividades falhou:", str(e))

def testar_get_atividades():
    try:
        r = requests.get("http://127.0.0.1:5002/atividades")
        print("19. GET /atividades:", r.status_code, r.json())
    except requests.exceptions.RequestException as e:
        print("19. GET /atividades falhou:", str(e))


# Execução dos testes
if __name__ == "__main__":
    testar_reset()  # Teste 1

    professor_id = testar_post_professor()  # Teste 2
    if professor_id:
        testar_get_professores()            # Teste 3

        turma_id = testar_post_turma(professor_id)  # Teste 5
        if turma_id:
            testar_get_turmas()                      # Teste 6

            aluno_id = testar_post_aluno(turma_id)   # Teste 8
            if aluno_id:
                testar_get_alunos()                  # Teste 9
                testar_put_aluno(aluno_id, turma_id) # Teste 10
                testar_delete_aluno(aluno_id)        # Teste 11

            testar_put_turma(turma_id, professor_id) # Teste 13
            testar_post_reserva(turma_id)            # Teste 16
            testar_get_reservas()                    # Teste 17
            testar_delete_turma(turma_id)            # Teste 7

        testar_put_professor(professor_id)           # Teste 12
        testar_post_atividade(professor_id)          # Teste 18
        testar_get_atividades()                      # Teste 19
        testar_delete_professor(professor_id)        # Teste 4

    testar_get_home()     # Teste 14
    testar_get_swagger()  # Teste 15