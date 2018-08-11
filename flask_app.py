from flask import Flask, render_template, request, redirect
from flask_sslify import SSLify
import pandas as pd


app = Flask(__name__)
#sslify = SSLify(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)