from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Events Server version 1.0.0"
    
@app.route("/events", methods=["POST"])
def add_events():
    user_event = request.get_json()
    print(user_event)
    return jsonify("OK")