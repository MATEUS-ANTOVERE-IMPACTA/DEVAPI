from flask import Blueprint, jsonify, request
from models.professor import Professor
from config import db

professor_bp = Blueprint("professor_bp", __name__)

@professor_bp.route("", methods=["GET"])
def listar_professores():
    professores = Professor.query.all()
    return jsonify([professor.to_dict() for professor in professores])

@professor_bp.route("", methods=["POST"])
def criar_professor():
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({'erro': 'Nome do professor é obrigatório'}), 400

    novo_professor = Professor(nome=data['nome'])
    db.session.add(novo_professor)
    db.session.commit()
    return jsonify(novo_professor.to_dict()), 201

@professor_bp.route("/<int:id>", methods=["GET"])
def obter_professor(id):
    professor = Professor.query.get(id)
    if not professor:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    return jsonify(professor.to_dict())

@professor_bp.route("/<int:id>", methods=["PUT"])
def atualizar_professor(id):
    professor = Professor.query.get(id)
    if not professor:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    data = request.get_json()
    professor.nome = data.get('nome', professor.nome)
    db.session.commit()
    return jsonify(professor.to_dict())

@professor_bp.route("/<int:id>", methods=["DELETE"])
def deletar_professor(id):
    professor = Professor.query.get(id)
    if not professor:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    db.session.delete(professor)
    db.session.commit()
    return jsonify({'mensagem': 'Professor removido com sucesso'}), 200