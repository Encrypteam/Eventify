import unittest
from swagger_server.services.event_service import EventService
from unittest.mock import Mock, patch
from swagger_server.repositories.event_repository import EventRepository
import datetime as dt


class TestEventService(unittest.TestCase):

    def setUp(self):
        self.event_repository = EventRepository()

    def test_get_event_success(self):
        mock_repository = Mock(name='get_event_by_id')
        mock_repository.return_value = {'id': 1, 'description': 'test', 'date': '2021-01-01',
                                        'latitude': 1.0, 'longitude': 1.0, 'capacity': 1}

        with patch.object(self.event_repository, 'get_event_by_id', mock_repository):
            self.eventService = EventService(self.event_repository)
            event = self.eventService.get_event(1)

        mock_repository.assert_called_once()
        assert event == {'id': 1, 'description': 'test', 'date': '2021-01-01',
                         'latitude': 1.0, 'longitude': 1.0, 'capacity': 1}, "Should be equal"

    def test_get_event_fail(self):
        mock_repository = Mock(name='get_event_by_id')
        mock_repository.return_value = None

        with patch.object(self.event_repository, 'get_event_by_id', mock_repository):
            self.eventService = EventService(self.event_repository)
            event = self.eventService.get_event(1)

        assert event is None, "Should not be an existing event"

    def test_get_events_include_past_events_success(self):
        mock_repository = Mock(name='get_events')
        mock_repository.return_value = [{'id': 1, 'description': 'test', 'date': '2021-01-01',
                                         'latitude': 1.0, 'longitude': 1.0, 'capacity': 1},
                                        {'id': 2, 'description': 'test', 'date': '2025-01-01',
                                         'latitude': 1.0, 'longitude': 1.0, 'capacity': 1},
                                        {'id': 3, 'description': 'test', 'date': '2026-01-01',
                                         'latitude': 1.0, 'longitude': 1.0, 'capacity': 1}]

        with patch.object(self.event_repository, 'get_events', mock_repository):
            self.eventService = EventService(self.event_repository)
            events = self.eventService.get_events(True)

        assert len(events) == 3, "Should be 3 events"

    def test_get_only_future_events_success(self):
        mock_repository = Mock(name='get_events')
        mock_repository.return_value = [
            {'id': 1, 'description': 'test', 'date': dt.datetime.now() - dt.timedelta(days=10),
             'latitude': 1.0, 'longitude': 1.0, 'capacity': 1},
            {'id': 2, 'description': 'test', 'date': dt.datetime.now() + dt.timedelta(days=36),
             'latitude': 1.0, 'longitude': 1.0, 'capacity': 1},
            {'id': 3, 'description': 'test', 'date': dt.datetime.now() + dt.timedelta(days=30),
             'latitude': 1.0, 'longitude': 1.0, 'capacity': 1}]

        with patch.object(self.event_repository, 'get_events', mock_repository):
            self.eventService = EventService(self.event_repository)
            events = self.eventService.get_events(False)
        assert len(list(events)) == 2, "Should be 2 events"

    def test_create_event_success(self):
        mock_repository = Mock(name='create_event')
        mock_repository.return_value = {'id': 1, 'description': 'test', 'date': '2023-06-01',
                                        'latitude': 1.0, 'longitude': 1.0, 'capacity': 1}

        with patch.object(self.event_repository, 'create_event', mock_repository):
            self.event_service = EventService(self.event_repository)
            event_data = {
                'description': 'test',
                'date': '2023-06-01',
                'latitude': 1.0,
                'longitude': 1.0,
                'capacity': 1
            }
            event = self.event_repository.create_event(event_data)

        mock_repository.assert_called_once_with(event_data)
        assert event == {'id': 1, 'description': 'test', 'date': '2023-06-01',
                         'latitude': 1.0, 'longitude': 1.0, 'capacity': 1}, "Should be equal"

    def test_update_event_success(self):
        mock_repository = Mock(name='update_event')
        mock_repository.return_value = {'id': 1, 'description': 'updated test', 'date': '2023-06-01',
                                        'latitude': 1.0, 'longitude': 1.0, 'capacity': 1}

        with patch.object(self.event_repository, 'update_event', mock_repository):
            self.event_service = EventService(self.event_repository)
            event_data = {
                'id': 1,
                'description': 'updated test',
                'date': '2023-06-01',
                'latitude': 1.0,
                'longitude': 1.0,
                'capacity': 1
            }
            event = self.event_repository.update_event(event_data)

        mock_repository.assert_called_once_with(event_data)
        assert event == {'id': 1, 'description': 'updated test', 'date': '2023-06-01',
                         'latitude': 1.0, 'longitude': 1.0, 'capacity': 1}, "Should be equal"

    def test_delete_event_success(self):
        mock_repository = Mock(name='delete_event')
        mock_repository.return_value = True

        with patch.object(self.event_repository, 'delete_event', mock_repository):
            self.event_service = EventService(self.event_repository)
            result = self.event_repository.delete_event(1)

        mock_repository.assert_called_once_with(1)
        assert result is True, "Should be True"

if __name__ == '__main__':
    unittest.main()