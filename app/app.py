from flask import Flask
from controllers.aluno_controller import aluno_bp
from controllers.professor_controller import professor_bp
from controllers.turma_controller import turma_bp
from controllers.reset_controller import reset_bp
from config import db
from flasgger import Swagger

app = Flask(__name__)

# Configurações
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 5000
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER'] = {
    "title": "DevAPI - Documentação com Swagger",
    "uiversion": 3
}

# Inicializa banco e Swagger
db.init_app(app)
swagger = Swagger(app)

# Registra os Blueprints
app.register_blueprint(aluno_bp, url_prefix="/alunos")
app.register_blueprint(professor_bp, url_prefix="/professores")
app.register_blueprint(turma_bp, url_prefix="/turmas")
app.register_blueprint(reset_bp)  # <-- sem prefixo para evitar duplicação

@app.route('/')
def home():
    return '🚀 Bem-vindo à API DevAPI! Acesse a documentação Swagger em /apidocs/'

# Cria as tabelas no banco
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])