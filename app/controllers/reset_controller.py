from flask import Blueprint, jsonify
from config import db
from models.aluno import Aluno
from models.professor import Professor
from models.turma import Turma

reset_bp = Blueprint("reset_bp", __name__)

@reset_bp.route("/reseta", methods=["POST"])
def resetar_dados():
    """
    Reseta todos os dados do banco de dados
    ---
    tags:
      - Utilitários
    responses:
      200:
        description: Dados resetados com sucesso
    """
    db.session.query(Aluno).delete()
    db.session.query(Turma).delete()
    db.session.query(Professor).delete()
    db.session.commit()
    return jsonify({"mensagem": "Dados resetados com sucesso"}), 200