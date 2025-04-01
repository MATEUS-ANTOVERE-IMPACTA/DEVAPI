from flask import Flask, jsonify, request
from models.aluno import Aluno
from models.professor import Professor
from models.turma import Turma

app = Flask(__name__)

professores = []
turmas = []
alunos = []

# ==================== PROFESSORES ====================

@app.route('/professores', methods=['GET'])
def get_professores():
    return jsonify([p.to_dict() for p in professores])

@app.route('/professores', methods=['POST'])
def create_professor():
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({'erro': 'professor sem nome'}), 400
    novo_professor = Professor(len(professores) + 1, data['nome'])
    professores.append(novo_professor)
    return jsonify(novo_professor.to_dict()), 200

@app.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    professor = next((p for p in professores if p.id == id), None)
    if not professor:
        return jsonify({'erro': 'professor nao encontrado'}), 400
    return jsonify(professor.to_dict())

@app.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    professor = next((p for p in professores if p.id == id), None)
    if not professor:
        return jsonify({'erro': 'professor nao encontrado'}), 400
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({'erro': 'professor sem nome'}), 400
    professor.nome = data['nome']
    return jsonify(professor.to_dict()), 200

@app.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    global professores
    professor = next((p for p in professores if p.id == id), None)
    if not professor:
        return jsonify({'erro': 'professor nao encontrado'}), 400
    professores = [p for p in professores if p.id != id]
    return jsonify({'mensagem': 'Professor removido'}), 200

# ==================== TURMAS ====================

@app.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify([t.to_dict() for t in turmas])

@app.route('/turmas', methods=['POST'])
def create_turma():
    data = request.get_json()
    if 'descricao' not in data or 'professor_id' not in data or 'ativo' not in data:
        return jsonify({'erro': 'dados insuficientes para turma'}), 400
    professor = next((p for p in professores if p.id == data['professor_id']), None)
    if not professor:
        return jsonify({'erro': 'professor nao encontrado para turma'}), 400
    nova_turma = Turma(len(turmas) + 1, data['descricao'], data['professor_id'], data['ativo'])
    turmas.append(nova_turma)
    return jsonify(nova_turma.to_dict()), 200

@app.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    turma = next((t for t in turmas if t.id == id), None)
    if not turma:
        return jsonify({'erro': 'turma nao encontrada'}), 400
    return jsonify(turma.to_dict())

@app.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    global turmas
    turma = next((t for t in turmas if t.id == id), None)
    if not turma:
        return jsonify({'erro': 'turma nao encontrada'}), 400
    turmas = [t for t in turmas if t.id != id]
    return jsonify({'mensagem': 'Turma removida'}), 200

# ==================== ALUNOS ====================

@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify([a.to_dict() for a in alunos])

@app.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.get_json()
    campos_obrigatorios = ['nome', 'idade', 'turma_id', 'data_nascimento', 'nota_primeiro_semestre', 'nota_segundo_semestre']
    for campo in campos_obrigatorios:
        if campo not in data:
            return jsonify({'erro': f'aluno sem {campo}'}), 400
    turma = next((t for t in turmas if t.id == data['turma_id']), None)
    if not turma:
        return jsonify({'erro': 'turma nao encontrada para o aluno'}), 400
    novo_aluno = Aluno(len(alunos) + 1, data['nome'], data['idade'], data['turma_id'], data['data_nascimento'], data['nota_primeiro_semestre'], data['nota_segundo_semestre'])
    alunos.append(novo_aluno)
    return jsonify(novo_aluno.to_dict()), 200

@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    global alunos
    aluno = next((a for a in alunos if a.id == id), None)
    if not aluno:
        return jsonify({'erro': 'aluno nao encontrado'}), 400
    alunos = [a for a in alunos if a.id != id]
    return jsonify({'mensagem': 'Aluno removido'}), 200

# ==================== RESET ====================

@app.route('/reseta', methods=['POST', 'DELETE'])
def reset_data():
    global professores, turmas, alunos
    professores, turmas, alunos = [], [], []
    return jsonify({'mensagem': 'Dados resetados'}), 200

# ==================== EXECUÇÃO ====================

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)
