from flask import Flask, jsonify, request

app = Flask(__name__)

professores = []
turmas = []
alunos = []

# ==================== PROFESSORES ====================

@app.route('/professores', methods=['GET'])
def get_professores():
    """Lista todos os professores"""
    return jsonify(professores)

@app.route('/professores', methods=['POST'])
def create_professor():
    """Cria um novo professor"""
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({'erro': 'professor sem nome'}), 400
    data['id'] = len(professores) + 1
    professores.append(data)
    return jsonify(data), 200

@app.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    """Obtém um professor pelo ID"""
    professor = next((p for p in professores if p['id'] == id), None)
    if not professor:
        return jsonify({'erro': 'professor nao encontrado'}), 400
    return jsonify(professor)

@app.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    """Atualiza o nome de um professor"""
    professor = next((p for p in professores if p['id'] == id), None)
    if not professor:
        return jsonify({'erro': 'professor nao encontrado'}), 400
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({'erro': 'professor sem nome'}), 400
    professor['nome'] = data['nome']
    return jsonify(professor), 200

@app.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    """Deleta um professor pelo ID"""
    global professores
    professor = next((p for p in professores if p['id'] == id), None)
    if not professor:
        return jsonify({'erro': 'professor nao encontrado'}), 400
    professores = [p for p in professores if p['id'] != id]
    return jsonify({'mensagem': 'Professor removido'}), 200

# ==================== TURMAS ====================

@app.route('/turmas', methods=['GET'])
def get_turmas():
    """Lista todas as turmas"""
    return jsonify(turmas)

@app.route('/turmas', methods=['POST'])
def create_turma():
    """Cria uma nova turma"""
    data = request.get_json()
    if 'descricao' not in data or 'professor_id' not in data or 'ativo' not in data:
        return jsonify({'erro': 'dados insuficientes para turma'}), 400
    professor = next((p for p in professores if p['id'] == data['professor_id']), None)
    if not professor:
        return jsonify({'erro': 'professor nao encontrado para turma'}), 400
    data['id'] = len(turmas) + 1
    turmas.append(data)
    return jsonify(data), 200

@app.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    """Obtém uma turma pelo ID"""
    turma = next((t for t in turmas if t['id'] == id), None)
    if not turma:
        return jsonify({'erro': 'turma nao encontrada'}), 400
    return jsonify(turma)

@app.route('/turmas/<int:id>', methods=['PUT'])
def update_turma(id):
    """Atualiza a descrição de uma turma"""
    turma = next((t for t in turmas if t['id'] == id), None)
    if not turma:
        return jsonify({'erro': 'turma nao encontrada'}), 400
    data = request.get_json()
    if 'descricao' not in data:
        return jsonify({'erro': 'descricao obrigatoria'}), 400
    turma['descricao'] = data['descricao']
    return jsonify(turma), 200

@app.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    """Deleta uma turma pelo ID"""
    global turmas
    turma = next((t for t in turmas if t['id'] == id), None)
    if not turma:
        return jsonify({'erro': 'turma nao encontrada'}), 400
    turmas = [t for t in turmas if t['id'] != id]
    return jsonify({'mensagem': 'Turma removida'}), 200

# ==================== ALUNOS ====================

@app.route('/alunos', methods=['GET'])
def get_alunos():
    """Lista todos os alunos"""
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def create_aluno():
    """Cria um novo aluno e calcula a média final"""
    data = request.get_json()
    campos_obrigatorios = ['nome', 'idade', 'turma_id', 'data_nascimento', 'nota_primeiro_semestre', 'nota_segundo_semestre']
    for campo in campos_obrigatorios:
        if campo not in data:
            return jsonify({'erro': f'aluno sem {campo}'}), 400
    turma = next((t for t in turmas if t['id'] == data['turma_id']), None)
    if not turma:
        return jsonify({'erro': 'turma nao encontrada para o aluno'}), 400
    data['media_final'] = (data['nota_primeiro_semestre'] + data['nota_segundo_semestre']) / 2
    data['id'] = len(alunos) + 1
    alunos.append(data)
    return jsonify(data), 200

@app.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    """Obtém um aluno pelo ID"""
    aluno = next((a for a in alunos if a['id'] == id), None)
    if not aluno:
        return jsonify({'erro': 'aluno nao encontrado'}), 400
    return jsonify(aluno)

@app.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    """Atualiza os dados do aluno e recalcula a média final"""
    aluno = next((a for a in alunos if a['id'] == id), None)
    if not aluno:
        return jsonify({'erro': 'aluno nao encontrado'}), 400
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({'erro': 'aluno sem nome'}), 400
    aluno['nome'] = data['nome']
    if 'nota_primeiro_semestre' in data:
        aluno['nota_primeiro_semestre'] = data['nota_primeiro_semestre']
    if 'nota_segundo_semestre' in data:
        aluno['nota_segundo_semestre'] = data['nota_segundo_semestre']
    if 'nota_primeiro_semestre' in data or 'nota_segundo_semestre' in data:
        aluno['media_final'] = (aluno['nota_primeiro_semestre'] + aluno['nota_segundo_semestre']) / 2
    return jsonify(aluno), 200

@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    """Deleta um aluno pelo ID"""
    global alunos
    aluno = next((a for a in alunos if a['id'] == id), None)
    if not aluno:
        return jsonify({'erro': 'aluno nao encontrado'}), 400
    alunos = [a for a in alunos if a['id'] != id]
    return jsonify({'mensagem': 'Aluno removido'}), 200

# ==================== RESET ====================

@app.route('/reseta', methods=['POST', 'DELETE'])
def reset_data():
    """Reseta todos os dados da aplicação"""
    global professores, turmas, alunos
    professores, turmas, alunos = [], [], []
    return jsonify({'mensagem': 'Dados resetados'}), 200

# ==================== EXECUÇÃO ====================

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)