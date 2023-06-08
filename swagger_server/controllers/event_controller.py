import connexion
import six

from swagger_server.models.event import Event  # noqa: E501
from swagger_server import util


def events_id_inscriptions_guid_get(event_id):  # noqa: E501
    """Find event by ID

    Return inscription for one user (guid) # noqa: E501

    :param event_id: ID of event to return
    :type event_id: int

    :rtype: Event
    """
    return 'do some magic!'


def find_events_by_status(status=None):  # noqa: E501
    """Finds Events by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: str

    :rtype: List[Event]
    """
    return 'do some magic!'


def get_event_by_id(event_id):  # noqa: E501
    """Find event by ID

    Returns a single event # noqa: E501

    :param event_id: ID of event to return
    :type event_id: int

    :rtype: Event
    """
    return 'do some magic!'


def update_event_with_form(event_id, name=None, surname=None, telephone=None, dni=None, mail=None):  # noqa: E501
    """Inscription in an event

     # noqa: E501

    :param event_id: ID of event that needs to be updated
    :type event_id: int
    :param name: Name of the user
    :type name: str
    :param surname: Surname of the user
    :type surname: str
    :param telephone: Telephone of the user
    :type telephone: int
    :param dni: dni of the user
    :type dni: int
    :param mail: mail of the user
    :type mail: str

    :rtype: None
    """
    return 'do some magic!'


def upload_file(invitation_code, body=None):  # noqa: E501
    """upload_file

     # noqa: E501

    :param invitation_code: Delete inscription
    :type invitation_code: int
    :param body: 
    :type body: dict | bytes

    :rtype: Event
    """
    return 'do some magic!'
