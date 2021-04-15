from flask import Flask, render_template, request
from flask_cors import CORS
from .config  import init_blueprints
from .middlewares import middlewares

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return render_template('index.html')

app.before_request_funcs = middlewares

init_blueprints(app)
