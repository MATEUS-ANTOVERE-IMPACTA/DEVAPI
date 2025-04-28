from flask import Blueprint, jsonify, request
from models.aluno import Aluno
from config import db

aluno_bp = Blueprint("aluno_bp", __name__)

@aluno_bp.route("", methods=["GET"])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos])

@aluno_bp.route("", methods=["POST"])
def criar_aluno():
    data = request.get_json()
    campos_obrigatorios = ['nome', 'idade', 'turma_id', 'data_nascimento', 'nota_primeiro_semestre', 'nota_segundo_semestre']
    for campo in campos_obrigatorios:
        if campo not in data:
            return jsonify({'erro': f'aluno sem {campo}'}), 400

    novo_aluno = Aluno(
        nome=data['nome'],
        idade=data['idade'],
        turma_id=data['turma_id'],
        data_nascimento=data['data_nascimento'],
        nota_primeiro_semestre=data['nota_primeiro_semestre'],
        nota_segundo_semestre=data['nota_segundo_semestre']
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify(novo_aluno.to_dict()), 201

@aluno_bp.route("/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify({'erro': 'Aluno não encontrado'}), 404
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({'mensagem': 'Aluno removido com sucesso'}), 200