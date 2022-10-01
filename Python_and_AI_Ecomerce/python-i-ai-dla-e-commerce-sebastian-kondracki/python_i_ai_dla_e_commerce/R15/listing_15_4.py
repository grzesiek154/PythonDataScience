from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from flask_sqlalchemy import SQLAlchemy
from flask_expects_json import expects_json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ue.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class UserEvent(db.Model):
    id = db.Column("user_event_id", db.Integer, primary_key=True)
    user = db.Column(db.String(50))
    event = db.Column(db.String(50))
    product = db.Column(db.String(50))
    def __init__(self, user, event, product):
        self.user = user
        self.event = event
        self.product = product
db.create_all()
schema = {
    "type": "object",
    "properties": {
        "user": {"type": "string", "minLength": 5},
        "event": {"type": "string", "minLength": 4},
        "product": {"type": "string", "minLength": 8},
},
    "required": ["user", "event", "product"],
}

@app.route("/")
def welcome():
    return "Events Server version 1.0.0"

@app.route("/events", methods=["POST"])
@expects_json(schema)
def add_events():
    user_event = request.get_json()
    db.session.add(
        UserEvent(user_event["user"], user_event["event"], user_event["product"])
    )
    db.session.commit()
    return Response(status=201)