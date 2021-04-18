from flask import Blueprint
from ..crud import save_record, get_record, update_record, delete_record
from ...collections.countries import Countries
from ...schemas.country_schema import SaveCountryInput

bp = Blueprint('country', __name__, url_prefix='/api/')

@bp.route('/countries/<id>', methods=['GET'])
def get(id):
    return get_record(id, Countries, __name__, get.__name__)

@bp.route('/countries', methods=['POST'])
def save():
    return save_record(SaveCountryInput, Countries, __name__, save.__name__), 201

@bp.route('/countries/<id>', methods=['PUT'])
def update(id):
    return update_record(id, SaveCountryInput, Countries, __name__, update.__name__)

@bp.route('/countries/<id>', methods=['DELETE'])
def delete(id):
    return delete_record(id, Countries, __name__, delete.__name__), 204
