from flask import Blueprint
from ..crud import save_record, get_record
from ...collections import Roles
from ...schemas import SaveRoleInput

bp = Blueprint('role', __name__, url_prefix='/api/')

@bp.route('/roles/<id>', methods=['GET'])
def get(id):
    return get_record(id, Roles, __name__, get.__name__)

@bp.route('/roles', methods=['POST'])
def save():
    return save_record(SaveRoleInput, Roles, __name__, save.__name__)
