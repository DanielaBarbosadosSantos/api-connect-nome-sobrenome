# API Connect - MVP de Gerenciamento de Usuários

## 🎯 Objetivo da API
A **API Connect** é um Produto Mínimo Viável (MVP) desenvolvido em arquitetura back-end modular para o gerenciamento de usuários. O projeto foi estruturado seguindo rigorosamente os princípios RESTful e a separação de responsabilidades (Separation of Concerns - SoC).

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Framework:** Flask (microframework web)
* **Controle de Versão:** Git e GitHub

## 🚀 Como Executar o Projeto Localmente
1. Clonar o repositório: `git clone https://github.com/daniela-barbosa/api-connect-daniela-santos.git`
2. Criar ambiente virtual: `python -m venv venv`
3. Ativar ambiente virtual: `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Linux/macOS)
4. Instalar dependências: `pip install flask`
5. Executar a aplicação: `python app.py`

## 📋 Tabela de Referência de Endpoints
* **POST** `/api/users/` - Cadastra um novo usuário (`201 Created` / `400 Bad Request`)
* **GET** `/api/users/` - Retorna a listagem geral (`200 OK`)
* **GET** `/api/users/<id>` - Busca um usuário por ID (`200 OK` / `404 Not Found`)
* **PUT** `/api/users/<id>` - Atualiza os dados de um usuário (`200 OK` / `404 Not Found`)
* **DELETE** `/api/users/<id>` - Remove um usuário (`200 OK` / `404 Not Found`)

