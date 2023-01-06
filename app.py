from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return("Hello world!!!!! 06.01.2023 kl 20:43")
