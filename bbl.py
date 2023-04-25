from flask import Flask, redirect, render_template, request, session
import jsonify
import pandas as pd
from main import get_matches

app = Flask(__name__, template_folder="./templates")

@app.route("/", methods=["GET", "POST"])
def matches():
    if request.method == "GET":
        df = pd.read_csv("all_region.csv")
        url = df.loc[df["team_name"].str.contains("bbl"), "url"].values[0]
        data = get_matches(url)
        return render_template("index.html", data=data)
    else:
        pass

if __name__ == "__main__":
    app.run(debug=True)