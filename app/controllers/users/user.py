from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/api/')

@bp.route('/users', methods=['POST'])
def save():
    try:
        pass

    except:
        pass
