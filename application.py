from flask import Flask, render_template
import boto3
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', nome='cassiano')

@app.route("/usuarios")
def usuarios():

    ec2 = boto3.resource('ec2', region='sa-east-1')

    instancias = ec2.instances.all()

    listadeinstancia = [tag['Value'] for instancia in instancias for tag in instancia.tags if tag['Key'] == "Name"]

    pprint(listadeinstancia)

    return render_template('usuarios.html', listadeinstancia=listadeinstancia)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
