import requests
import unittest

'''
Cada aluno será representado por um dicionário JSON como o seguinte: 
{"id":1,"nome":"marcos"}

Testes 000 e 001:
Na URL /alunos, se o verbo for GET, 
retornaremos uma lista com um dicionário para cada aluno.

Na URL /alunos, com o verbo POST, ocorrerá a criação do aluno,
enviando um desses dicionários 

Teste 002
Na URL /alunos/<int:id>, se o verbo for GET, devolveremos o nome e id do aluno. 
(exemplo. /alunos/2 devolve o dicionário do aluno(a) de id 2)

Teste 003
Na URL /reseta, apagaremos a lista de alunos e professores (essa URL só atende o verbo POST e DELETE).

Teste 004
Na URL /alunos/<int:id>, se o verbo for DELETE, deletaremos o aluno.
(dica: procure lista.remove)

Teste 005
Na URL /alunos/<int:id>, se o verbo for PUT, 
editaremos o aluno, mudando seu nome. 
Para isso, o usuário vai enviar um dicionário 
com a chave nome, que deveremos processar

Se o usuário manda um dicionário {“nome”:”José”} para a url /alunos/40,
com o verbo PUT, trocamos o nome do usuário 40 para José

Tratamento de erros

Testes 006 a 008b: Erros de usuário darão um código de status 400, e retornarão um dicionário descrevendo o erro. 
No teste 006, tentamos fazer GET, PUT e DELETE na URL  /alunos/15, sendo que o aluno de id 15 não existe. Nesse caso, devemos retornar um código de status 400 e um dicionário {“erro”:'aluno nao encontrado'}
No teste 007, tentamos criar dois alunos com a mesma id. Nesse caso, devemos retornar um código de status 400 e um dicionário {‘erro’:'id ja utilizada'}
No teste 008a, tento enviar um aluno sem nome via post. Nesse caso, devemos retornar um código de status 400 e um dicionário {‘erro’:'aluno sem nome'}
No teste 008b, tento editar um aluno, usando o verbo put, mas mando um dicionário sem nome. Nesse caso, devemos retornar um código de status 400 e um dicionário {“erro”:'aluno sem nome'}
Testes 100 a 109: Teremos as URLs análogas para professores.


'''

BASE_URL = "http://localhost:5000"

class TestAPIEndpoints(unittest.TestCase):
    def setUp(self):
        # Reseta os dados (professores, turmas e alunos) antes de cada teste
        r = requests.post(f"{BASE_URL}/reseta")
        self.assertEqual(r.status_code, 200)

    # ==================== TESTES PARA PROFESSORES ====================
    def test_create_professor(self):
        """Cria um professor e verifica se o id é gerado e o nome está correto."""
        data = {
            "nome": "Carlos",
            "idade": 45,
            "materia": "Matemática",
            "observacoes": "Doutor em álgebra"
        }
        r = requests.post(f"{BASE_URL}/professores", json=data)
        self.assertEqual(r.status_code, 200)
        resp = r.json()
        self.assertIn("id", resp)
        self.assertEqual(resp["nome"], "Carlos")

    def test_list_professors(self):
        """Lista os professores cadastrados."""
        requests.post(f"{BASE_URL}/professores", json={"nome": "Ana", "idade": 38, "materia": "Biologia"})
        r = requests.get(f"{BASE_URL}/professores")
        self.assertEqual(r.status_code, 200)
        lista = r.json()
        self.assertTrue(len(lista) > 0)

    def test_get_professor(self):
        """Obtém um professor pelo ID."""
        r = requests.post(f"{BASE_URL}/professores", json={"nome": "João", "idade": 50, "materia": "Física"})
        prof_id = r.json()["id"]
        r_get = requests.get(f"{BASE_URL}/professores/{prof_id}")
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()["nome"], "João")

    def test_update_professor(self):
        """Atualiza o nome de um professor existente."""
        r = requests.post(f"{BASE_URL}/professores", json={"nome": "João", "idade": 50, "materia": "Física"})
        prof_id = r.json()["id"]
        r_update = requests.put(f"{BASE_URL}/professores/{prof_id}", json={"nome": "João Silva"})
        self.assertEqual(r_update.status_code, 200)
        r_check = requests.get(f"{BASE_URL}/professores/{prof_id}")
        self.assertEqual(r_check.json()["nome"], "João Silva")

    def test_delete_professor(self):
        """Exclui um professor e verifica que não é encontrado."""
        r = requests.post(f"{BASE_URL}/professores", json={"nome": "Marta", "idade": 42, "materia": "Química"})
        prof_id = r.json()["id"]
        r_del = requests.delete(f"{BASE_URL}/professores/{prof_id}")
        self.assertEqual(r_del.status_code, 200)
        r_check = requests.get(f"{BASE_URL}/professores/{prof_id}")
        self.assertIn(r_check.status_code, [400, 404])
        self.assertEqual(r_check.json()["erro"], "professor nao encontrado")

    # ==================== TESTES PARA TURMAS ====================
    def test_create_turma(self):
        """Cria uma turma com professor válido e verifica se o id é gerado."""
        # Cria um professor primeiro
        r_prof = requests.post(f"{BASE_URL}/professores", json={"nome": "Ricardo", "idade": 40, "materia": "História"})
        prof_id = r_prof.json()["id"]
        data_turma = {
            "descricao": "Turma A",
            "professor_id": prof_id,
            "ativo": True
        }
        r_turma = requests.post(f"{BASE_URL}/turmas", json=data_turma)
        self.assertEqual(r_turma.status_code, 200)
        resp = r_turma.json()
        self.assertIn("id", resp)
        self.assertEqual(resp["descricao"], "Turma A")

    def test_list_turmas(self):
        """Lista as turmas cadastradas."""
        # Cria uma turma válida
        r_prof = requests.post(f"{BASE_URL}/professores", json={"nome": "Luciana", "idade": 35, "materia": "Geografia"})
        prof_id = r_prof.json()["id"]
        requests.post(f"{BASE_URL}/turmas", json={"descricao": "Turma B", "professor_id": prof_id, "ativo": True})
        r = requests.get(f"{BASE_URL}/turmas")
        self.assertEqual(r.status_code, 200)
        self.assertTrue(len(r.json()) > 0)

    def test_get_turma(self):
        """Obtém uma turma pelo ID."""
        r_prof = requests.post(f"{BASE_URL}/professores", json={"nome": "Marcos", "idade": 47, "materia": "Literatura"})
        prof_id = r_prof.json()["id"]
        r_turma = requests.post(f"{BASE_URL}/turmas", json={"descricao": "Turma Original", "professor_id": prof_id, "ativo": True})
        turma_id = r_turma.json()["id"]
        r_get = requests.get(f"{BASE_URL}/turmas/{turma_id}")
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()["descricao"], "Turma Original")

    def test_update_turma(self):
        """Atualiza a descrição de uma turma existente."""
        r_prof = requests.post(f"{BASE_URL}/professores", json={"nome": "Marcos", "idade": 47, "materia": "Literatura"})
        prof_id = r_prof.json()["id"]
        r_turma = requests.post(f"{BASE_URL}/turmas", json={"descricao": "Turma Original", "professor_id": prof_id, "ativo": True})
        turma_id = r_turma.json()["id"]
        r_update = requests.put(f"{BASE_URL}/turmas/{turma_id}", json={"descricao": "Turma Atualizada"})
        self.assertEqual(r_update.status_code, 200)
        self.assertEqual(r_update.json()["descricao"], "Turma Atualizada")

    def test_delete_turma(self):
        """Exclui uma turma e verifica que não é encontrada."""
        r_prof = requests.post(f"{BASE_URL}/professores", json={"nome": "Paula", "idade": 36, "materia": "Sociologia"})
        prof_id = r_prof.json()["id"]
        r_turma = requests.post(f"{BASE_URL}/turmas", json={"descricao": "Turma X", "professor_id": prof_id, "ativo": True})
        turma_id = r_turma.json()["id"]
        r_del = requests.delete(f"{BASE_URL}/turmas/{turma_id}")
        self.assertEqual(r_del.status_code, 200)
        r_check = requests.get(f"{BASE_URL}/turmas/{turma_id}")
        self.assertIn(r_check.status_code, [400, 404])
        self.assertEqual(r_check.json()["erro"], "turma nao encontrada")

    def test_create_turma_invalid_professor(self):
        """Tenta criar uma turma com um professor inexistente e verifica o erro."""
        data_turma = {
            "descricao": "Turma Y",
            "professor_id": 999,  # Professor inexistente
            "ativo": True
        }
        r = requests.post(f"{BASE_URL}/turmas", json=data_turma)
        self.assertIn(r.status_code, [400, 404])
        self.assertEqual(r.json()["erro"], "professor nao encontrado para turma")

    # ==================== TESTES PARA ALUNOS ====================
    def test_create_aluno(self):
        """Cria um aluno com turma válida e verifica o cálculo da média final."""
        # Cria um professor e turma primeiro
        r_prof = requests.post(f"{BASE_URL}/professores", json={"nome": "Fernanda", "idade": 35, "materia": "Geografia"})
        prof_id = r_prof.json()["id"]
        r_turma = requests.post(f"{BASE_URL}/turmas", json={"descricao": "Turma B", "professor_id": prof_id, "ativo": True})
        turma_id = r_turma.json()["id"]
        aluno_data = {
            "nome": "Lucas",
            "idade": 16,
            "turma_id": turma_id,
            "data_nascimento": "2008-12-01",
            "nota_primeiro_semestre": 8.0,
            "nota_segundo_semestre": 7.0
        }
        r_aluno = requests.post(f"{BASE_URL}/alunos", json=aluno_data)
        self.assertEqual(r_aluno.status_code, 200)
        resp = r_aluno.json()
        self.assertIn("id", resp)
        # Verifica se a média final foi calculada corretamente
        self.assertAlmostEqual(resp["media_final"], 7.5, places=1)

    def test_list_alunos(self):
        """Lista os alunos cadastrados."""
        r = requests.get(f"{BASE_URL}/alunos")
        self.assertEqual(r.status_code, 200)
        self.assertIsInstance(r.json(), list)

    def test_get_aluno(self):
        """Obtém um aluno pelo ID."""
        r_prof = requests.post(f"{BASE_URL}/professores", json={"nome": "Mariana", "idade": 32, "materia": "Português"})
        prof_id = r_prof.json()["id"]
        r_turma = requests.post(f"{BASE_URL}/turmas", json={"descricao": "Turma Z", "professor_id": prof_id, "ativo": True})
        turma_id = r_turma.json()["id"]
        aluno_data = {
            "nome": "Eduardo",
            "idade": 17,
            "turma_id": turma_id,
            "data_nascimento": "2006-09-20",
            "nota_primeiro_semestre": 7.0,
            "nota_segundo_semestre": 8.0
        }
        r_aluno = requests.post(f"{BASE_URL}/alunos", json=aluno_data)
        aluno_id = r_aluno.json()["id"]
        r_get = requests.get(f"{BASE_URL}/alunos/{aluno_id}")
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.json()["nome"], "Eduardo")

    def test_update_aluno(self):
        """Atualiza o nome e as notas de um aluno e verifica a recalculação da média final."""
        # Cria os dados iniciais
        r_prof = requests.post(f"{BASE_URL}/professores", json={"nome": "Roberta", "idade": 30, "materia": "Química"})
        prof_id = r_prof.json()["id"]
        r_turma = requests.post(f"{BASE_URL}/turmas", json={"descricao": "Turma C", "professor_id": prof_id, "ativo": True})
        turma_id = r_turma.json()["id"]
        aluno_data = {
            "nome": "Marcos",
            "idade": 17,
            "turma_id": turma_id,
            "data_nascimento": "2007-06-15",
            "nota_primeiro_semestre": 6.0,
            "nota_segundo_semestre": 6.0
        }
        r_aluno = requests.post(f"{BASE_URL}/alunos", json=aluno_data)
        aluno_id = r_aluno.json()["id"]
        # Atualiza o aluno
        r_update = requests.put(f"{BASE_URL}/alunos/{aluno_id}", json={
            "nome": "Marcos Silva",
            "nota_primeiro_semestre": 7.0,
            "nota_segundo_semestre": 8.0
        })
        self.assertEqual(r_update.status_code, 200)
        resp = r_update.json()
        self.assertEqual(resp["nome"], "Marcos Silva")
        self.assertAlmostEqual(resp["media_final"], 7.5, places=1)

    def test_delete_aluno(self):
        """Exclui um aluno e verifica que não é encontrado posteriormente."""
        r_prof = requests.post(f"{BASE_URL}/professores", json={"nome": "Pedro", "idade": 40, "materia": "História"})
        prof_id = r_prof.json()["id"]
        r_turma = requests.post(f"{BASE_URL}/turmas", json={"descricao": "Turma D", "professor_id": prof_id, "ativo": True})
        turma_id = r_turma.json()["id"]
        r_aluno = requests.post(f"{BASE_URL}/alunos", json={
            "nome": "Bianca",
            "idade": 15,
            "turma_id": turma_id,
            "data_nascimento": "2009-03-10",
            "nota_primeiro_semestre": 9.0,
            "nota_segundo_semestre": 8.0
        })
        aluno_id = r_aluno.json()["id"]
        r_del = requests.delete(f"{BASE_URL}/alunos/{aluno_id}")
        self.assertEqual(r_del.status_code, 200)
        r_check = requests.get(f"{BASE_URL}/alunos/{aluno_id}")
        self.assertIn(r_check.status_code, [400, 404])
        self.assertEqual(r_check.json()["erro"], "aluno nao encontrado")

    def test_create_aluno_invalid_turma(self):
        """Tenta criar um aluno com turma inexistente e verifica o erro."""
        aluno_data = {
            "nome": "Ricardo",
            "idade": 18,
            "turma_id": 999,  # Turma inexistente
            "data_nascimento": "2005-11-20",
            "nota_primeiro_semestre": 7.0,
            "nota_segundo_semestre": 7.5
        }
        r = requests.post(f"{BASE_URL}/alunos", json=aluno_data)
        self.assertIn(r.status_code, [400, 404])
        self.assertEqual(r.json()["erro"], "turma nao encontrada para o aluno")

    # ==================== TESTE PARA RESETAR TODOS OS DADOS ====================
    def test_reset_data(self):
        """Cria dados e depois reseta, verificando que todas as listas ficaram vazias."""
        # Cria um professor, turma e aluno
        requests.post(f"{BASE_URL}/professores", json={"nome": "Teste", "idade": 30, "materia": "Teste"})
        r = requests.post(f"{BASE_URL}/reseta")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(requests.get(f"{BASE_URL}/professores").json()), 0)
        self.assertEqual(len(requests.get(f"{BASE_URL}/turmas").json()), 0)
        self.assertEqual(len(requests.get(f"{BASE_URL}/alunos").json()), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)