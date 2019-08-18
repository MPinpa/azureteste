from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', nome='cassiano')

@app.route("/usuarios")
def cadastro():
    with open('usuarios.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()

    return '{}'.format(conteudo)