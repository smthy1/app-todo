# 🌎 To-Do API

This task management app is built with FastAPI and PostgreSQL, fully packaged with Docker. It's a project to practice and apply what I've learned.


## 📦 Features
📝 Create tasks
📋 List all tasks
🔍 Search task by title
✅ Mark task as completed
🗑️ Delete task by title


## ⚙️ Technologies used
 - Python 3.12.10
 - FastAPI
 - PostgreSQL
 - Psycopg (async)
 - Docker

## 📜 Requirements

 - Docker installed - [Download](https://www.docker.com)
 - Postman or any other API testing tool (optional) - [Download](https://www.postman.com/downloads/)


## 🚀 How to run

1. Clone this repository:

```bash
   git clone https://github.com/smthy1/api-todo.git
   cd api-todo
```

2. Build and start the containers:

```bash
    docker-compose up --build -d
```

3. Wait a few seconds fpr Docker build and start the containers, then you're ready to test the API with Postman, Insomnia, or any tool prefer.
 - Base URL: http://localhost:8000/todo

4. Available endpoints:

 - POST /todo - Create a task
 - GET /todo - List all tasks
 - GET /todo/{task_title} - Search task by title
 - PUT /todo/{task_title} - Mark task as completed
 - DELETE /todo/{task_title} - Delete task by title

5. Additional notes:

 - You can also test the API via Swagger UI: http://localhost:8000/docs
 
 - To explore the database visually, access pgAdmin4 at http://localhost:15432 
        - Login: api@gmail.com 
        - Password: postgres

 - After running the docker-comopose command, you don't need to keep the repository files locally, since Docker will handle everything inside the containers. You can safely delete the repo clone if you want.

## 🧠 What I learned
 - ✅ Building APIs with FastAPI
 - 🐘 Use PostgreSQL asynchronously with psycopg
 - 📦 Packaging an app with Docker 
 - 🔗 Container-to-container communication
 - 📄 Project organization and backend best practices

## 🤝 Contributing

Feel free to open issues or submit pull requests with suggestions or improvements!

# ✉️ Contact:

Developed by [smthy1](https://github.com/smthy1). Contacte me via [email](mailto:luiz.smith.br@gmail.com)


# 🇧🇷 To-Do API

Este aplicativo de gerenciamento de tarefas foi feito com FastAPI, PostgreSQL e empacotado com Docker. O objetivo deste é colocar em prática o que aprendi.

## 📦 Funcionalidades
📝 Criar tarefas
📋 Listar todas as tarefas
🔍 Buscar tarefa pelo título
✅ Marcar tarefa como concluída
🗑️ Deletar tarefa pelo título

## ⚙️ Tecnologias Utilizadas
 - Python 3.12.10

 - FastAPI

 - PostgreSQL

 - Psycopg (assíncrono)

 - Docker

## 📜 Requisitos
 
 - Docker instalado - [Download](https://www.docker.com)
 - Postman instalado ou qualquer outra ferramenta pra testar as rotas da API (optional) - [Download](https://www.postman.com/downloads/)

## 🚀 Como Executar
1. Clone este repositório:

```bash
   git clone https://github.com/smthy1/api-todo.git
   cd api-todo
```

2. Gere os containers:

```bash
    docker-compose up --build -d
```

3. Aguarde alguns segundos até o Docker gerar e iniciar os containers, depois disso você já pode testar a API com Postman, Insomnia ou qualquer outra ferramenta.

 - URL base: http://localhost:8000/todo

4. Endpoints disponíveis:

 - POST /todo — Criar tarefa

 - GET /todo — Listar todas as tarefas

 - GET /todo/{task_title} — Buscar tarefa pelo título

 - PUT /todo/{task_title} — Marcar tarefa como concluída

 - DELETE /todo/{task_title} — Deletar tarefa pelo título

5. Observações:

 - Você pode testar a API também via Swagger UI: http://localhost:8000/docs

 - Caso queira explorar o banco visualmente, acesse o pgAdmin4: http://localhost:15432
        Login: api@gmail.com
        Senha: postgres

 - Após rodar o comando docker-compose, não é necessário manter os arquivos do repositório localmente, pois o Docker já cuida de tudo dentro dos containers. Pode apagar o repositório sem problemas.

## 🧠 O que aprendi
 - ✅ Construir APIs com FastAPI

 - 🐘 Usar PostgreSQL com conexão assíncrona com psycopg

 - 📦 Empacotar aplicação com Docker

 - 🔗 Comunicação entre containers

 - 📄 Organização e boas práticas

## 🤝 Contribuições
Sinta-se à vontade para abrir issues ou enviar pull requests com sugestões e melhorias!

# ✉️ Contato
Desenvolvido por [smthy1](https://github.com/smthy1). Me contate via [email](mailto:luiz.smith.br@gmail.com)