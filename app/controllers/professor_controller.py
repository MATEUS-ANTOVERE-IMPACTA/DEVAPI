from flask import Blueprint, request, jsonify
from models.professor import Professor

professor_bp = Blueprint("professor_bp", __name__)

@professor_bp.route("", methods=["GET"])
def listar_professores():
    """
    Lista todos os professores
    ---
    tags:
      - Professores
    responses:
      200:
        description: Lista de professores
    """
    return jsonify(Professor.listar())

@professor_bp.route("", methods=["POST"])
def criar_professor():
    """
    Cria um novo professor
    ---
    tags:
      - Professores
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - nome
          properties:
            nome:
              type: string
    responses:
      201:
        description: Professor criado com sucesso
      400:
        description: Erro de validação
    """
    data = request.get_json()
    resposta, status = Professor.criar(data)
    return jsonify(resposta), status

@professor_bp.route("/<int:id>", methods=["PUT"])
def atualizar_professor(id):
    """
    Atualiza um professor pelo ID
    ---
    tags:
      - Professores
    parameters:
      - in: path
        name: id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - nome
          properties:
            nome:
              type: string
    responses:
      200:
        description: Professor atualizado
      404:
        description: Professor não encontrado
    """
    data = request.get_json()
    resposta, status = Professor.atualizar(id, data)
    return jsonify(resposta), status

@professor_bp.route("/<int:id>", methods=["DELETE"])
def deletar_professor(id):
    """
    Remove um professor pelo ID
    ---
    tags:
      - Professores
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Professor removido
      404:
        description: Professor não encontrado
    """
    resposta, status = Professor.deletar(id)
    return jsonify(resposta), status