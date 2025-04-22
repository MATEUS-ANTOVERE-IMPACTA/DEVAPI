from flask import Blueprint, jsonify
from storage import alunos, professores, turmas

reset_bp = Blueprint("reset_bp", __name__)

@reset_bp.route('/reseta', methods=['POST', 'DELETE'])
def reset_data():
    alunos.clear()
    professores.clear()
    turmas.clear()
    return jsonify({'mensagem': 'Dados resetados com sucesso'}), 200