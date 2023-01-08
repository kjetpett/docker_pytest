from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return("Hello world!!!!! 09.01.2023 kl 00:20")
