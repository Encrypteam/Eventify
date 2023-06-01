from swagger_server.repositories.event_repository import EventRepository
from datetime import datetime


class EventService:

    def __init__(self, repository):
        if repository is None:
            self.event_repository = EventRepository()
        else:
            self.event_repository = repository

    def get_event(self, event_id):
        return self.event_repository.get_event_by_id(event_id)

    def get_events(self, past_events=False):
        events = self.event_repository.get_events()
        if not past_events:
            #TODO: fix this filter
            events = filter(lambda x: x.date > datetime.now(), events)
        print(events)
        return events