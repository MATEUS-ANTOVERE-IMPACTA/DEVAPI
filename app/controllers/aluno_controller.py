from flask import Blueprint, jsonify, request
from models.aluno import Aluno

aluno_bp = Blueprint('aluno_bp', __name__)
alunos = []
turmas = []  # Simulação temporária até a centralização dos dados no db.py

@aluno_bp.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify([a.to_dict() for a in alunos])

@aluno_bp.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.get_json()
    campos = ['nome', 'idade', 'turma_id', 'data_nascimento', 'nota_primeiro_semestre', 'nota_segundo_semestre']
    for campo in campos:
        if campo not in data:
            return jsonify({'erro': f'aluno sem {campo}'}), 400

    turma = next((t for t in turmas if t.id == data['turma_id']), None)
    if not turma:
        return jsonify({'erro': 'turma nao encontrada para o aluno'}), 400

    novo_aluno = Aluno(
        id=len(alunos) + 1,
        nome=data['nome'],
        idade=data['idade'],
        turma_id=data['turma_id'],
        data_nascimento=data['data_nascimento'],
        nota_primeiro_semestre=data['nota_primeiro_semestre'],
        nota_segundo_semestre=data['nota_segundo_semestre']
    )
    alunos.append(novo_aluno)
    return jsonify(novo_aluno.to_dict()), 200

@aluno_bp.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    global alunos
    aluno = next((a for a in alunos if a.id == id), None)
    if not aluno:
        return jsonify({'erro': 'aluno nao encontrado'}), 400
    alunos = [a for a in alunos if a.id != id]
    return jsonify({'mensagem': 'Aluno removido'}), 200
