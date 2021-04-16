from flask import Blueprint
from ..crud import save_record

bp = Blueprint('user', __name__, url_prefix='/api/')

@bp.route('/users', methods=['POST'])
def save():
    pass
