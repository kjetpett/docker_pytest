from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return("Hello world!!!!! 30.10 kl23:31")
