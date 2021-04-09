from flask import Flask, render_template
from .config  import init_blueprints

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

init_blueprints(app)
