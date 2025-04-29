from flask import Blueprint, request, jsonify
from models.professor import Professor

professor_bp = Blueprint("professor_bp", __name__)

@professor_bp.route("", methods=["GET"])
def listar_professores():
    return jsonify(Professor.listar())

@professor_bp.route("", methods=["POST"])
def criar_professor():
    data = request.get_json()
    resposta, status = Professor.criar(data)
    return jsonify(resposta), status

@professor_bp.route("/<int:id>", methods=["DELETE"])
def deletar_professor(id):
    resposta, status = Professor.deletar(id)
    return jsonify(resposta), status