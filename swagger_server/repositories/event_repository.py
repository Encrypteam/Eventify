from swagger_server.models.db.event_db import EventModel
from swagger_server.__main__ import db
from datetime import datetime
class EventRepository():

    def __init__(self):
        self.events = EventModel

    def get_event_by_id(self, event_id):
        return db.session.query(self.events).get(event_id)

    def find_events_by_status(self, status=None):
        return db.session.query(self.events).filter_by(status=status)

    """def find_future_events(self):
        return db.session.query(self.events).filter(self.events.date >= datetime.now())"""

    def update_event_with_form(self, event_id, name=None, surname=None, telephone=None, dni=None, mail=None):
        return db.session.query(self.events).get(event_id)

    def events_id_inscriptions_guid_get(self, event_id):
        return db.session.query(self.events).get(event_id)

    def get_events(self):
        return db.session.query(self.events).all()

    def create_event(self, event):
        db.session.add(event)
        db.session.commit()
        return event

    def update_event(self, event_id, data):
        event = db.session.query(self.events).get(event_id)
        for key, value in data:
            setattr(event, key, value)
        db.session.add(event)
        db.session.commit()
        return event

    def delete_event(self, event_id):
        event = db.session.query(self.events).get(event_id)
        db.session.delete(event)
        db.session.commit()
        return event