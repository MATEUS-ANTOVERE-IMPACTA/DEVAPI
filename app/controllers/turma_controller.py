from flask import Blueprint, jsonify, request
from models.turma import Turma

turma_bp = Blueprint('turma_bp', __name__)
turmas = []
professores = []  # Simulando acesso (será substituído via import/refatoração futura)

@turma_bp.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify([t.to_dict() for t in turmas])

@turma_bp.route('/turmas', methods=['POST'])
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

@turma_bp.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    turma = next((t for t in turmas if t.id == id), None)
    if not turma:
        return jsonify({'erro': 'turma nao encontrada'}), 400
    return jsonify(turma.to_dict())

@turma_bp.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    global turmas
    turma = next((t for t in turmas if t.id == id), None)
    if not turma:
        return jsonify({'erro': 'turma nao encontrada'}), 400
    turmas = [t for t in turmas if t.id != id]
    return jsonify({'mensagem': 'Turma removida'}), 200
