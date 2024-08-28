from flask import Flask
from textblob import TextBlob

api = Flask(__name__)
@api.route("/<frase>") # get

def sentimento(frase): 
    text = TextBlob(frase)
    polaridade = text.sentiment.polarity
    subjetividade = text.sentiment.subjectivity
    return f"A polaridade é {polaridade} e a subjetividade é {subjetividade}"

api.run(debug = True)
