from flask import Blueprint, request, jsonify
from models.aluno import Aluno

aluno_bp = Blueprint("aluno_bp", __name__)

@aluno_bp.route("", methods=["GET"])
def listar_alunos():
    """
    Lista todos os alunos
    ---
    tags:
      - Alunos
    responses:
      200:
        description: Lista de alunos
    """
    return jsonify(Aluno.listar())

@aluno_bp.route("", methods=["POST"])
def criar_aluno():
    """
    Cria um novo aluno
    ---
    tags:
      - Alunos
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - nome
            - idade
            - turma_id
            - data_nascimento
            - nota_primeiro_semestre
            - nota_segundo_semestre
          properties:
            nome:
              type: string
            idade:
              type: integer
            turma_id:
              type: integer
            data_nascimento:
              type: string
            nota_primeiro_semestre:
              type: number
            nota_segundo_semestre:
              type: number
    responses:
      201:
        description: Aluno criado com sucesso
      400:
        description: Erro de validação
    """
    data = request.get_json()
    resposta, status = Aluno.criar(data)
    return jsonify(resposta), status

@aluno_bp.route("/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    """
    Remove um aluno pelo ID
    ---
    tags:
      - Alunos
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Aluno removido com sucesso
      404:
        description: Aluno não encontrado
    """
    resposta, status = Aluno.deletar(id)
    return jsonify(resposta), status