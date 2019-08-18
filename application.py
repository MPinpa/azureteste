from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "acabei de criar minha propria app"
