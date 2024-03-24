
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/resources")
def resources():
    with open("resources.json", "r") as f:
        resources = json.load(f)
    return jsonify(resources)

if __name__ == "__main__":
    app.run(debug=True)
