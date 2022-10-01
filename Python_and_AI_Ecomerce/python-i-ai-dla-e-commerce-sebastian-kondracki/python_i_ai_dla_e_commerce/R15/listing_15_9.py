from flask import Flask
from flask import jsonify
from flask import request
from flask_expects_json import expects_json
import pickle
import os
import pandas as pd
app = Flask(__name__)

schema = {
    "type": "object",
    "properties": {
        "age": {"type": "integer"},
        "days": {"type": "integer"},
        "gender": {"type": "string"},
        "occupation": {"type": "string"},
        "reminder": {"type": "string"},
        "subscription": {"type": "string"},
},
    "required": ["age", "days", "gender", "occupation", "reminder", "subscription"],
}

base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, "churn.bin"), "rb") as reader:
    clf = pickle.load(reader)

@app.route("/")
def welcome():
    return "Churn Analyzer Server version 1.0.0"

@app.route("/customers", methods=["POST"])
@expects_json(schema)
def analize_customer():
    customer = request.get_json()
    data = [ {
                "age": customer["age"],
                "days": customer["days"],
                "gender": customer["gender"],
                "occupation": customer["occupation"],
                "reminder": customer["reminder"],
                "subscription": customer["subscription"],
    } ]
    X = pd.DataFrame(data=data)
    predictions = clf.predict_proba(X)
    result = {"resignation_no": predictions[0][0], "resignation_yes" : predictions[0][1]}
    return result