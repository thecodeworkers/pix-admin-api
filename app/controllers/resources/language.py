from flask import Blueprint
from ..crud import save_record, get_record, update_record, delete_record
from ...collections import Languages
from ...schemas import SaveLanguageInput

bp = Blueprint('language', __name__, url_prefix='/api/')

@bp.route('/languages/<id>', methods=['GET'])
def get(id):
    return get_record(id, Languages, __name__, get.__name__)

@bp.route('/languages', methods=['POST'])
def save():
    return save_record(SaveLanguageInput, Languages, __name__, save.__name__), 201

@bp.route('/languages/<id>', methods=['PUT'])
def update(id):
    return update_record(id, SaveLanguageInput, Languages, __name__, update.__name__)

@bp.route('/languages/<id>', methods=['DELETE'])
def delete(id):
    return delete_record(id, Languages, __name__, delete.__name__), 204
