from flask import Flask
from flask import jsonify
from datetime import datetime

app = Flask(__name__)
@app.route("/")
def welcome():
    return "Events Server version 1.0.0"

@app.route("/time")
def get_time():
    result = {"current_date_time" : datetime.now().strftime("%Y-%m-%d%H:%M:%S")}
    return jsonify(result)