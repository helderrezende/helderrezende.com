from flask import Blueprint, render_template

blog = Blueprint('blog', __name__, url_prefix='/blog', static_folder='static')

@blog.route('/')
def index():
    return render_template('index.html')


@blog.route('/diversifique')
def diversificacao():
    return render_template('diversificacao.html')