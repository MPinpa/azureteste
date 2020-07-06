from flask import Flask, render_template
import boto3
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', nome='cassiano')

@app.route("/usuarios")
def usuarios():

    s3 = boto3.resource('s3')

    buckets = s3.buckets.all()

    print(buckets)


    return render_template('usuarios.html', listadeinstancia=buckets)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
