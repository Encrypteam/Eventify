import connexion
import six

from swagger_server.models.event import Event  # noqa: E501
from swagger_server import util
from flask import Blueprint, request, jsonify

eventy = Blueprint('eventy', __name__, url_prefix='/events')


@eventy.route('/', methods=['GET'])
def events_get():
    return jsonify({'message': 'events_get'})

@eventy.route('/event/<int:id>/<int:guid>', methods=['GET'])
def events_id_inscriptions_guid_get(id, guid):

    response_data = {
        'id': id,
        'guid': guid,
        'message': 'events_id_inscriptions_guid_get'
    }

    return jsonify(response_data)


@eventy.route('/status', methods=['POST'])
def find_events_by_status(status=None):  # noqa: E501
    return jsonify({'message': 'find_events_by_status'})

@eventy.route('/<id>', methods=['GET'])
def get_event_by_id(id):
    return jsonify({'message': 'get_event_by_id'})
@eventy.route('/event/<id>', methods=['PUT'])
def update_event_with_form(id, name=None, surname=None, telephone=None, dni=None, mail=None):
    return jsonify({'message': 'update_event_with_form'})


@eventy.route('/file', methods=['POST'])
def upload_file():
    return jsonify({'message': 'upload_file'})

