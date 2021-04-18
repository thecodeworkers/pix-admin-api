from flask import Blueprint
from ..crud import save_record, get_record, delete_record, update_record, table_record
from ...collections.states import States
from ...schemas.state_schema import SaveStateInput

bp = Blueprint('state', __name__, url_prefix='/api/')

@bp.route('/states', methods=['GET'])
def table():
    pipeline = lambda search: [
        {
            '$lookup': {
                'from': 'cities',
                'localField': 'cities',
                'foreignField': '_id',
                'as': 'cities'
            }
        },
        { '$unwind': '$cities' },
        {
            '$group': {
                '_id': '$_id',
                'id': { '$first': { '$toString': '$_id' } },
                'country': { '$first': { '$toString': '$country' } },
                'name': { '$first': '$name' },
                'cities': {
                    '$push': {
                        'id': { '$toString': '$cities._id' },
                        'state': { '$toString': '$cities.state' },
                        'name': '$cities.name',
                    }
                },
            }
        },
        {
            '$project': {
                '_id': 0,
            }
        },
        {
            '$match': {
                '$or': [
                    { 'name': { '$regex': search, '$options': 'i' } },
                    { 'cities.name': { '$regex': search, '$options': 'i' } }
                ]
            }
        }
    ]

    return table_record(pipeline, {'name': 1}, States, __name__, table.__name__)

@bp.route('/states/<id>', methods=['GET'])
def get(id):
    return get_record(id, States, __name__, get.__name__)

@bp.route('/states', methods=['POST'])
def save():
    return save_record(SaveStateInput, States, __name__, save.__name__), 201

@bp.route('/states/<id>', methods=['PUT'])
def update(id):
    return update_record(id, SaveStateInput, States, __name__, update.__name__)

@bp.route('/states/<id>', methods=['DELETE'])
def delete(id):
    return delete_record(id, States, __name__, delete.__name__), 204
