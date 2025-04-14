from flask import Blueprint, jsonify, request
from models.professor import Professor
from storage import professores

professor_bp = Blueprint("professor_bp", __name__)

@professor_bp.route("", methods=["GET"])
def listar_professores():
    return jsonify([p.to_dict() for p in professores])

@professor_bp.route("", methods=["POST"])
def criar_professor():
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({'erro': 'professor sem nome'}), 400
    novo_professor = Professor(len(professores) + 1, data['nome'])
    professores.append(novo_professor)
    return jsonify(novo_professor.to_dict()), 200

@professor_bp.route("/<int:id>", methods=["GET"])
def obter_professor(id):
    professor = next((p for p in professores if p.id == id), None)
    if not professor:
        return jsonify({'erro': 'professor nao encontrado'}), 400
    return jsonify(professor.to_dict())

@professor_bp.route("/<int:id>", methods=["PUT"])
def atualizar_professor(id):
    professor = next((p for p in professores if p.id == id), None)
    if not professor:
        return jsonify({'erro': 'professor nao encontrado'}), 400
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({'erro': 'professor sem nome'}), 400
    professor.nome = data['nome']
    return jsonify(professor.to_dict()), 200

@professor_bp.route("/<int:id>", methods=["DELETE"])
def deletar_professor(id):
    global professores
    professor = next((p for p in professores if p.id == id), None)
    if not professor:
        return jsonify({'erro': 'professor nao encontrado'}), 400
    professores = [p for p in professores if p.id != id]
    return jsonify({'mensagem': 'Professor removido'}), 200