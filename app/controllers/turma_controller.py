from flask import Blueprint, request, jsonify
from models.turma import Turma

turma_bp = Blueprint("turma_bp", __name__)

@turma_bp.route("", methods=["GET"])
def listar_turmas():
    return jsonify(Turma.listar())

@turma_bp.route("", methods=["POST"])
def criar_turma():
    data = request.get_json()
    resposta, status = Turma.criar(data)
    return jsonify(resposta), status

@turma_bp.route("/<int:id>", methods=["DELETE"])
def deletar_turma(id):
    resposta, status = Turma.deletar(id)
    return jsonify(resposta), status