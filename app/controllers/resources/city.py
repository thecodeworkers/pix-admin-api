from flask import Blueprint
from ..crud import save_record, get_record, update_record, delete_record, table_record
from ...collections.cities import Cities
from ...schemas.city_schema import SaveCityInput

bp = Blueprint('city', __name__, url_prefix='/api/')

@bp.route('/cities', methods=['GET'])
def table():
    pipeline = lambda search: [
        {
            '$match': {
                '$or': [
                    {'name': {'$regex': search, '$options': 'i'}},
                ]
            }
        },
        {
            '$group': {
                '_id': '$_id',
                'id': {'$first': {'$toString': '$_id'}},
                'name': {'$first': '$name'},
                'state': {'$first': {'$toString': '$state'}},
            }
        },
        {
            '$project': {
                '_id': 0
            }
        }
    ]

    return table_record(pipeline, {'name': 1}, Cities, __name__, table.__name__)

@bp.route('/cities/<id>', methods=['GET'])
def get(id):
    return get_record(id, Cities, __name__, get.__name__)

@bp.route('/cities', methods=['POST'])
def save():
    return save_record(SaveCityInput, Cities, __name__, save.__name__), 201

@bp.route('/cities/<id>', methods=['PUT'])
def update(id):
    return update_record(id, SaveCityInput, Cities, __name__, update.__name__)

@bp.route('/cities/<id>', methods=['DELETE'])
def delete(id):
    return delete_record(id, Cities, __name__, delete.__name__), 204
