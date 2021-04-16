from flask import Blueprint
from ..crud import save_record, get_record, update_record, delete_record
from ...collections import Permissions
from ...schemas import SavePermissionInput

bp = Blueprint('permission', __name__, url_prefix='/api/')

@bp.route('/permissions/<id>', methods=['GET'])
def get(id):
    return get_record(id, Permissions, __name__, get.__name__)

@bp.route('/permissions', methods=['POST'])
def save():
    return save_record(SavePermissionInput, Permissions, __name__, save.__name__), 201

@bp.route('/permissions/<id>', methods=['PUT'])
def update(id):
    return update_record(id, SavePermissionInput, Permissions, __name__, update.__name__)

@bp.route('/permissions/<id>', methods=['DELETE'])
def delete(id):
    return delete_record(id, Permissions, __name__, delete.__name__), 204
