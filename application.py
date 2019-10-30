from flask import Flask, render_template
import boto3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', nome='cassiano')

@app.route("/usuarios")
def usuarios():

    ec2 = boto3.resource('ec2')

    listadeinstancia = ec2.instances.all()

    return render_template('usuarios.html', usuarios=listadeinstancia)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
