from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    text = request.form["text"]
    source = request.form["source"]
    target = request.form["target"]
    translated_text = translator.translate(text, src=source, dest=target).text
    return render_template("index.html", translated=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
