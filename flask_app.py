from flask import Flask, render_template, request, redirect
from flask_sslify import SSLify
import pandas as pd
from blog import blog

app = Flask(__name__)   
app.register_blueprint(blog)
#sslify = SSLify(app)

@app.route('/')
def index():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True)