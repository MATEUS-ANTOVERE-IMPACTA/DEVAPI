from flask import Blueprint, request, jsonify
from models.turma import Turma

turma_bp = Blueprint("turma_bp", __name__)

@turma_bp.route("", methods=["GET"])
def listar_turmas():
    """
    Lista todas as turmas
    ---
    tags:
      - Turmas
    responses:
      200:
        description: Lista de turmas
    """
    return jsonify(Turma.listar())

@turma_bp.route("", methods=["POST"])
def criar_turma():
    """
    Cria uma nova turma
    ---
    tags:
      - Turmas
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - descricao
            - professor_id
          properties:
            descricao:
              type: string
            professor_id:
              type: integer
            ativo:
              type: boolean
    responses:
      201:
        description: Turma criada com sucesso
      400:
        description: Erro de validação
    """
    data = request.get_json()
    resposta, status = Turma.criar(data)
    return jsonify(resposta), status

@turma_bp.route("/<int:id>", methods=["DELETE"])
def deletar_turma(id):
    """
    Remove uma turma pelo ID
    ---
    tags:
      - Turmas
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Turma removida com sucesso
      404:
        description: Turma não encontrada
    """
    resposta, status = Turma.deletar(id)
    return jsonify(resposta), status