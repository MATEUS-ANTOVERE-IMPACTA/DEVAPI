# 📚 DevAPI - Sistema de Gerenciamento Acadêmico

Bem-vindo ao **DevAPI**, uma API RESTful desenvolvida em **Python com Flask**, ideal para gerenciamento de alunos, professores e turmas. O projeto segue o padrão arquitetural **MVC**, utiliza banco de dados **SQLite**, e oferece documentação interativa via **Swagger UI**.

---

## 🚀 Funcionalidades

### 📌 Alunos

- Cadastro, listagem e remoção de alunos.
- Cálculo automático da média final (1º e 2º semestre).
- Validação de existência da turma.

### 👨‍🏫 Professores

- Cadastro, listagem e remoção de professores.

### 🏫 Turmas

- Cadastro de turmas vinculadas aos professores.
- Listagem e remoção de turmas.
- Controle de status "**ativo**".

### 🧹 Reset

- Rota específica para resetar todas as entidades do banco de dados.

### 🧾 Documentação com Swagger UI

- Interface gráfica para testes e documentação das rotas.
- Disponível em: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **Flask 3.0.2**
- **Flask-SQLAlchemy**
- **Flasgger (Swagger UI)**
- **SQLite** (banco de dados leve e embutido)
- **Docker & Docker Compose**

---

## 🐳 Como Rodar com Docker

Clone o repositório:

```bash
git clone https://github.com/MATEUS-ANTOVERE-IMPACTA/DEVAPI
cd DEVAPI
Execute via Docker Compose:

bash
Copiar
Editar
docker-compose up --build
🌐 Acesse a aplicação
Swagger UI: http://localhost:5000/apidocs

API: http://localhost:5000

📂 Estrutura do Projeto
arduino
Copiar
Editar
DEVAPI/
├── app/
│   ├── controllers/
│   │   ├── aluno_controller.py
│   │   ├── professor_controller.py
│   │   ├── turma_controller.py
│   │   └── reset_controller.py
│   ├── models/
│   │   ├── aluno.py
│   │   ├── professor.py
│   │   └── turma.py
│   ├── config.py
│   └── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── teste.py
🧪 Testes
Você pode testar a API executando diretamente o arquivo teste.py:

python teste.py

👨‍💼 Equipe de Desenvolvimento
Mateus Antovere Silva Rosário | RA: 2401764

Leandro Ferreira Cassemiro Rosa | RA: 2302060

Gabriel Quaglio Monteiro Praça | RA: 2400738
