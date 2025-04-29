from flask import Blueprint, request, jsonify
from models.aluno import Aluno

aluno_bp = Blueprint("aluno_bp", __name__)

@aluno_bp.route("", methods=["GET"])
def listar_alunos():
    return jsonify(Aluno.listar())

@aluno_bp.route("", methods=["POST"])
def criar_aluno():
    data = request.get_json()
    resposta, status = Aluno.criar(data)
    return jsonify(resposta), status

@aluno_bp.route("/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    resposta, status = Aluno.deletar(id)
    return jsonify(resposta), status