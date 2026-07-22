from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "AI Exam Invigilation Backend Running"


@app.route("/status")
def status():

    phone = {
        "students": 0,
        "phones": 0
    }

    behavior = {
        "talking": False,
        "gesture": False
    }

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    phone_file = os.path.join(base_dir, "outputs", "phone_output.json")
    behavior_file = os.path.join(base_dir, "outputs", "behavior_output.json")

    if os.path.exists(phone_file):
        with open(phone_file, "r") as f:
            phone = json.load(f)

    if os.path.exists(behavior_file):
        with open(behavior_file, "r") as f:
            behavior = json.load(f)

    return jsonify({
        "students": phone["students"],
        "phones": phone["phones"],
        "talking": behavior["talking"],
        "gesture": behavior["gesture"]
    })


if __name__ == "__main__":
    app.run(debug=True)