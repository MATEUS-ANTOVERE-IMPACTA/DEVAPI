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
              example: João da Silva
            idade:
              type: integer
              example: 20
            turma_id:
              type: integer
              example: 1
            data_nascimento:
              type: string
              example: "2000-05-15"
            nota_primeiro_semestre:
              type: number
              example: 7.5
            nota_segundo_semestre:
              type: number
              example: 8.0
    responses:
      201:
        description: Aluno criado com sucesso
      400:
        description: Erro de validação
    """
    data = request.get_json()
    resposta, status = Aluno.criar(data)
    return jsonify(resposta), status

@aluno_bp.route("/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    """
    Atualiza um aluno existente
    ---
    tags:
      - Alunos
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
            - idade
            - turma_id
            - data_nascimento
            - nota_primeiro_semestre
            - nota_segundo_semestre
          properties:
            nome:
              type: string
              example: João da Silva Atualizado
            idade:
              type: integer
              example: 21
            turma_id:
              type: integer
              example: 1
            data_nascimento:
              type: string
              example: "2000-05-15"
            nota_primeiro_semestre:
              type: number
              example: 8.0
            nota_segundo_semestre:
              type: number
              example: 9.0
    responses:
      200:
        description: Aluno atualizado com sucesso
      400:
        description: Erro de validação
      404:
        description: Aluno não encontrado
    """
    data = request.get_json()
    resposta, status = Aluno.atualizar(id, data)
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