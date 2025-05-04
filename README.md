# 📚 DevAPI - Sistema de Gerenciamento Acadêmico

Bem-vindo ao **DevAPI**, uma API RESTful desenvolvida em **Python com Flask**, ideal para o gerenciamento de **alunos, professores e turmas**. O projeto segue o padrão MVC, utiliza banco de dados SQLite e oferece documentação via **Swagger**.

---

## 🚀 Funcionalidades

- 📌 **Alunos**
  - Cadastro, listagem e remoção de alunos.
  - Cálculo automático da média final (1º e 2º semestre).
  - Validação de turma existente.

- 👨‍🏫 **Professores**
  - Cadastro, listagem e remoção de professores.

- 🏫 **Turmas**
  - Cadastro de turmas vinculadas a professores.
  - Listagem e remoção de turmas.
  - Controle de status "ativo".

- 🧹 **Reset**
  - Rota para resetar todas as entidades do banco.

- 🧾 **Swagger**
  - Interface para documentação e testes das rotas.
  - Disponível em: [`/apidocs`](http://localhost:5000/apidocs)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11
- Flask 3.0.2
- Flask-SQLAlchemy
- Flasgger (Swagger UI)
- SQLite (banco de dados leve e embutido)
- Docker & Docker Compose

---

## 🐳 Rodando com Docker

1. Clone o repositório:
   ```bash
   git clone <https://github.com/MATEUS-ANTOVERE-IMPACTA/DEVAPI>
   cd DEVAPI
   ```

2. Rode o Docker:
   ```bash
   docker-compose up --build
   ```

3. Acesse:
   - Swagger UI: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)
   - API: [http://localhost:5000](http://localhost:5000)

---

## 📂 Estrutura de Pastas

```
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
```

---

## 🧪 Testes

Você pode testar a API executando o arquivo `teste.py`:

```bash
python teste.py
```

---

## 👨‍💻 Desenvolvido por

👤 Mateus Antovere Silva Rosário | RA: 2401764<br>
👤 Leandro Ferreira Cassemiro Rosa | RA: 2302060<br>
👤 Gabriel Quaglio Monteiro Praça | RA: 2400738
