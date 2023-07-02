from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    englishText = request.args.get('textToTranslate')
    frenchText = translator.englishToFrench(englishText)
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    frenchText = request.args.get('textToTranslate')
    englishText = translator.frenchToEnglish(frenchText)
    return englishText

@app.route("/")
def renderIndexPage():
    render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
