from flask import Flask, render_template
from flask_cors import CORS
from .config  import init_blueprints, error_handler, init_db
from .middlewares import middlewares

app = Flask(__name__)
app.secret_key = b'\x9b\x0f\xe7\xc6\xdcJu\xb5\xeb\xaf\xbft\x1d\xed\x98@'
CORS(app)

init_db()

@app.route('/')
def welcome():
    return render_template('index.html')

error_handler(app)

app.before_request_funcs = middlewares

init_blueprints(app)
