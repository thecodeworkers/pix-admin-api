from flask import Blueprint
from ..crud import save_record

bp = Blueprint('user', __name__, url_prefix='/api/')

@bp.route('/users', methods=['POST'])
def save():
    return save_record('', '', __name__, save.__name__)
