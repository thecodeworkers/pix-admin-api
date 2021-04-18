from flask import Blueprint
from ..crud import save_record, get_record, update_record, delete_record, table_record
from ...collections.countries import Countries
from ...schemas.country_schema import SaveCountryInput

bp = Blueprint('country', __name__, url_prefix='/api/')

@bp.route('/countries', methods=['GET'])
def table():
    pipeline = lambda search: [
        {
            '$lookup': {
                'from': 'states',
                'localField': 'states',
                'foreignField': '_id',
                'as': 'states'
            }
        },
        { '$unwind': '$states' },
        {
            '$lookup': {
                'from': 'cities',
                'localField': 'states.cities',
                'foreignField': '_id',
                'as': 'states.cities'
            }
        },
        {
            '$addFields': {
                'ref_id': '$_id',
                'states.cities': {
                    '$map': {
                        'input': '$states.cities',
                        'as': 'cities',
                        'in': {
                            'id': { '$toString': '$$cities._id' },
                            'name': '$$cities.name',
                            'state': { '$toString': '$$cities.state' }
                        }
                    }
                }
            }
        },
        {
            '$group': {
                '_id': '$_id',
                'id': { '$first': { '$toString': '$_id' } },
                'name': { '$first': '$name' },
                'code': { '$first': '$code'},
                'phone_prefix': { '$first': '$phone_prefix' },
                'active': { '$first': '$active' },
                'states': {
                    '$push': {
                        'id': { '$toString': '$states._id' },
                        'country': { '$toString': '$states.country' },
                        'name': '$states.name',
                        'cities': '$states.cities'
                    }
                },
            }
        },
        {
            '$project': {
                '_id': 0,
                'ref_id': 0
            }
        },
        {
            '$match': {
                '$or': [
                    { 'name': { '$regex': search, '$options': 'i' } },
                    { 'states.name': { '$regex': search, '$options': 'i' } },
                    { 'states.cities.name': { '$regex': search, '$options': 'i' } }
                ]
            }
        }
    ]

    return table_record(pipeline, {'name': 1}, Countries, __name__, table.__name__)

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
