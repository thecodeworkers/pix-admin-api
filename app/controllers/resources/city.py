from flask import Blueprint
from ..crud import save_record, get_record, update_record, delete_record
from ...collections.countries import Countries
from ...schemas.country_schema import SaveCountryInput

bp = Blueprint('city', __name__, url_prefix='/api/')

@bp.route('/cities/<id>', methods=['GET'])
def get(id):
    return get_record(id, Countries, __name__, get.__name__)

@bp.route('/cities', methods=['POST'])
def save():
    return save_record(SaveCountryInput, Countries, __name__, save.__name__), 201

@bp.route('/cities/<id>', methods=['PUT'])
def update(id):
    return update_record(id, SaveCountryInput, Countries, __name__, update.__name__)

@bp.route('/cities/<id>', methods=['DELETE'])
def delete(id):
    return delete_record(id, Countries, __name__, delete.__name__), 204
