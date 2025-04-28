from flask import Blueprint, jsonify, request
from models.turma import Turma
from config import db

turma_bp = Blueprint("turma_bp", __name__)

@turma_bp.route("", methods=["GET"])
def listar_turmas():
    turmas = Turma.query.all()
    return jsonify([turma.to_dict() for turma in turmas])

@turma_bp.route("", methods=["POST"])
def criar_turma():
    data = request.get_json()
    campos_obrigatorios = ['descricao', 'professor_id', 'ativo']
    for campo in campos_obrigatorios:
        if campo not in data:
            return jsonify({'erro': f'{campo} é obrigatório'}), 400

    nova_turma = Turma(
        descricao=data['descricao'],
        professor_id=data['professor_id'],
        ativo=data['ativo']
    )
    db.session.add(nova_turma)
    db.session.commit()
    return jsonify(nova_turma.to_dict()), 201

@turma_bp.route("/<int:id>", methods=["GET"])
def obter_turma(id):
    turma = Turma.query.get(id)
    if not turma:
        return jsonify({'erro': 'Turma não encontrada'}), 404
    return jsonify(turma.to_dict())

@turma_bp.route("/<int:id>", methods=["DELETE"])
def deletar_turma(id):
    turma = Turma.query.get(id)
    if not turma:
        return jsonify({'erro': 'Turma não encontrada'}), 404
    db.session.delete(turma)
    db.session.commit()
    return jsonify({'mensagem': 'Turma removida com sucesso'}), 200