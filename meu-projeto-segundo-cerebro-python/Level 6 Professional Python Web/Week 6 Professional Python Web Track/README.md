# Semana 6 – Python Profissional (Web)

**Objetivo:** Criar aplicações web com Flask, integrar banco de dados, implementar layouts responsivos e aplicar boas práticas de código.

---

## Segunda-feira – Configuração do Ambiente Web

### O que foi feito:

Instalação do Flask (pip install flask)

Estrutura básica de projeto Flask

Primeira rota / retornando "Hello, World!"

Executar servidor local (python app.py)

### Exemplo de código:

```from flask import Flask  # Import Flask

app = Flask(__name__)   # Create Flask app instance

@app.route("/")          # Define route for home page
def home():
    return "Hello, World!"  # Return simple message

if __name__ == "__main__":
    app.run(debug=True)  # Run server in debug mode
```
<br>


<br>

## Terça-feira – Rotas e Templates

### O que foi feito:

Criadas múltiplas rotas

Passagem de dados do Python para HTML

Templates com Jinja2

Estrutura de pastas: templates/ e static/

### Exemplo de código:

```@app.route("/hello/<name>")                 # Route with variable
def hello(name):
    return render_template("hello.html", name=name)  # Pass variable to template


Template hello.html:

<h1>Hello, {{ name }}!</h1>  <!-- Display variable from Python -->
```
<br>

<br>

## Quarta-feira – Formulários e Entrada de Dados

### O que foi feito:

Criado formulário HTML simples

Recebimento de dados via POST e GET

Validação básica

Exibição de respostas personalizadas

### Exemplo de código:

```@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":                # Check if form submitted
        name = request.form.get("name")        # Get input value
        return f"Hello {name}!"                # Return personalized message
    return render_template("form.html")        # Render form page
```
<br>

<br>

## Quinta-feira – Conexão com Banco de Dados

### O que foi feito:

Introdução ao SQLite no Flask

Criação e conexão com banco de dados

Inserção, consulta e listagem de dados

Exibição em páginas HTML

### Exemplo de código:

```import sqlite3

def get_db_connection():
    conn = sqlite3.connect("users.db")  # Connect to database
    conn.row_factory = sqlite3.Row       # Access rows by column name
    return conn
```
<br>

<br>

## Sexta-feira – CRUD Completo

### O que foi feito:

Sistema completo: Create, Read, Update, Delete

Funções separadas para cada operação

Interface simples para gerenciar registros

Boas práticas em rotas e banco

### Exemplo de código:

```@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    # Logic to update record
    pass
```
<br>

<br>

## Sábado – Layout e Finalização

### O que foi feito:

Adicionado CSS com Bootstrap

Navbar e layout padrão

Melhorada a responsividade

Revisão do código e testes

### Exemplo de código:

```<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<nav class="navbar navbar-dark bg-dark">...</nav>
```
<br>

<br>

## Domingo – Entrega Final e Testes Finais

### O que foi feito:

Projeto final integrando CRUD + Forms + Layout

Testes de entrada e validação de dados

Layout responsivo para mobile e desktop

Funcionalidades completas: Adicionar, Editar, Excluir usuários

Resumo do código final:

app.py → Flask + SQLite + rotas CRUD

templates/layout.html → Layout padrão com navbar

templates/index.html → Lista de usuários + formulário

templates/edit.html → Formulário de edição

### Exemplo de uso:

Acessar http://127.0.0.1:5000/

Adicionar, editar, excluir usuários

Layout responsivo e funcional

## Dicas e Boas Práticas da Semana 6
- Organize pastas: templates/, static/, app.py
- Valide todas entradas do usuário antes de inserir no banco
- Use Bootstrap para responsividade e consistência visual
- Separe lógica do banco em funções para código limpo
- Teste todas as rotas: GET, POST, Update, Delete
- Reaproveite templates com herança (layout.html)
- Comente sempre as partes importantes do código