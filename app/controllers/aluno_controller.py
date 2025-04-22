from flask import Blueprint, jsonify, request
from models.aluno import Aluno
from storage import alunos, turmas

aluno_bp = Blueprint("aluno_bp", __name__)

@aluno_bp.route("", methods=["GET"])
def listar_alunos():
    return jsonify([a.to_dict() for a in alunos])

@aluno_bp.route("", methods=["POST"])
def criar_aluno():
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

@aluno_bp.route("/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    global alunos
    aluno = next((a for a in alunos if a.id == id), None)
    if not aluno:
        return jsonify({'erro': 'aluno nao encontrado'}), 400
    alunos = [a for a in alunos if a.id != id]
    return jsonify({'mensagem': 'Aluno removido'}), 200