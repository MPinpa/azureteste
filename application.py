from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', nome='cassiano')

@app.route("/usuarios")
def usuarios():
    with open('usuarios.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()

    return render_template('usuarios.html', usuarios=conteudo)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
