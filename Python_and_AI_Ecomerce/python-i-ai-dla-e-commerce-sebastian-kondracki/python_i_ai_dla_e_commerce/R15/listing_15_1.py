from flask import Flask

app = Flask(__name__)
@app.route("/")
def welcome():
    return "Events Server version 1.0.0"