from flask import Flask, render_template, request
from main import run_pipeline

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        raw_text = request.form.get("raw_text")
        language = request.form.get("language")

        result = run_pipeline(raw_text, language)

        return render_template(
            "result.html",
            table=result["table"],
            route=result["route"],
            summary=result["summary"]
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
