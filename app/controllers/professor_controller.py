from flask import Blueprint, request, jsonify
from models.professor import Professor

professor_bp = Blueprint('professor_bp', __name__)
professores = []

@professor_bp.route('/professores', methods=['GET'])
def get_professores():
    return jsonify([p.to_dict() for p in professores]), 200

@professor_bp.route('/professores', methods=['POST'])
def create_professor():
    data = request.get_json()
    if 'nome' not in data or 'disciplina' not in data:
        return jsonify({'erro': 'Dados incompletos'}), 400
    novo_professor = Professor(len(professores) + 1, data['nome'], data['disciplina'])
    professores.append(novo_professor)
    return jsonify(novo_professor.to_dict()), 201

@professor_bp.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    professor = next((p for p in professores if p.p_id == id), None)
    if not professor:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    return jsonify(professor.to_dict()), 200

@professor_bp.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    professor = next((p for p in professores if p.p_id == id), None)
    if not professor:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    data = request.get_json()
    if 'nome' in data:
        professor.nome = data['nome']
    if 'disciplina' in data:
        professor.disciplina = data['disciplina']
    return jsonify(professor.to_dict()), 200

@professor_bp.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    global professores
    professor = next((p for p in professores if p.p_id == id), None)
    if not professor:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    professores = [p for p in professores if p.p_id != id]
    return jsonify({'mensagem': 'Professor removido'}), 200
