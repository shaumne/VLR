from flask import Flask, redirect, render_template, request
import jsonify
from main import get_matches

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def matches():
    if request.method == "GET":
        return get_matches()
    else:
        pass

if __name__ == "__main__":
    app.run(debug=True)