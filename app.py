from flask import Flask
from controllers.aluno_controller import aluno_bp
from controllers.professor_controller import professor_bp
from controllers.turma_controller import turma_bp

app = Flask(__name__)

# Registro dos Blueprints
app.register_blueprint(aluno_bp, url_prefix="/alunos")
app.register_blueprint(professor_bp, url_prefix="/professores")
app.register_blueprint(turma_bp, url_prefix="/turmas")

if __name__ == "__main__":
    app.run(debug=True)