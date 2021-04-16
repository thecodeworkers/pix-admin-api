from flask import Blueprint
from ..crud import save_record, get_record, update_record, delete_record
from ...collections.roles import Roles
from ...schemas.role_schema import SaveRoleInput

bp = Blueprint('role', __name__, url_prefix='/api/')

@bp.route('/roles/<id>', methods=['GET'])
def get(id):
    return get_record(id, Roles, __name__, get.__name__)

@bp.route('/roles', methods=['POST'])
def save():
    return save_record(SaveRoleInput, Roles, __name__, save.__name__), 201

@bp.route('/roles/<id>', methods=['PUT'])
def update(id):
    return update_record(id, SaveRoleInput, Roles, __name__, update.__name__)

@bp.route('/roles/<id>', methods=['DELETE'])
def delete(id):
    return delete_record(id, Roles, __name__, delete.__name__), 204
