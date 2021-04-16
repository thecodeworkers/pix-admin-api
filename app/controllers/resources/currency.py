from flask import Blueprint
from ..crud import save_record, get_record, update_record, delete_record
from ...collections.currencies import Currencies
from ...schemas.currency_schema import SaveCurrencyInput

bp = Blueprint('currency', __name__, url_prefix='/api/')

@bp.route('/currencies/<id>', methods=['GET'])
def get(id):
    return get_record(id, Currencies, __name__, get.__name__)

@bp.route('/currencies', methods=['POST'])
def save():
    return save_record(SaveCurrencyInput, Currencies, __name__, save.__name__), 201

@bp.route('/currencies/<id>', methods=['PUT'])
def update(id):
    return update_record(id, SaveCurrencyInput, Currencies, __name__, update.__name__)

@bp.route('/currencies/<id>', methods=['DELETE'])
def delete(id):
    return delete_record(id, Currencies, __name__, delete.__name__), 204
