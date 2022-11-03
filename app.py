from flask import Flask
import json

app = Flask(__name__)

@app.route("/first", methods=['GET'])
def read():
    with open("unicode.json","r")as f:
        a = json.load(f)
        return json.dumps(a)