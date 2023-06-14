import unittest
from swagger_server.repositories.event_repository import EventRepository
from swagger_server.models.db.event_db import EventModel
from datetime import datetime
from unittest.mock import Mock, patch


class TestEventRepository(unittest.TestCase):

    def setUp(self):
        self.event_model = EventModel()
        self.event_repository = EventRepository()

    def test_get_event_by_id_not_found(self):
        event_id = 1
        with patch('swagger_server.repositories.event_repository.db.session.query') as mock_query:
            mock_query.return_value.get.return_value = None
            event = self.event_repository.get_event_by_id(event_id)
        mock_query.assert_called_once_with(EventModel)
        mock_query.return_value.get.assert_called_once_with(event_id)
        assert event is None, "Should be None"

    def test_find_events_by_status_success(self):
        status = 'active'
        event_data = [{'id': 1, 'description': 'test', 'date': '2021-01-01',
                       'latitude': 1.0, 'longitude': 1.0, 'capacity': 1},
                      {'id': 2, 'description': 'test', 'date': '2022-01-01',
                       'latitude': 1.0, 'longitude': 1.0, 'capacity': 1}]
        with patch('swagger_server.repositories.event_repository.db.session.query') as mock_query:
            mock_query.return_value.filter_by.return_value = event_data
            events = self.event_repository.find_events_by_status(status)
        mock_query.assert_called_once_with(EventModel)
        mock_query.return_value.filter_by.assert_called_once_with(status=status)
        assert events == event_data, "Should be equal"

    def test_find_events_by_status_no_results(self):
        status = 'inactive'
        with patch('swagger_server.repositories.event_repository.db.session.query') as mock_query:
            mock_query.return_value.filter_by.return_value = []
            events = self.event_repository.find_events_by_status(status)
        mock_query.assert_called_once_with(EventModel)
        mock_query.return_value.filter_by.assert_called_once_with(status=status)
        assert events == [], "Should be an empty list"

    def test_get_events_success(self):
        event_data = [{'id': 1, 'description': 'test', 'date': '2021-01-01',
                       'latitude': 1.0, 'longitude': 1.0, 'capacity': 1},
                      {'id': 2, 'description': 'test', 'date': '2022-01-01',
                       'latitude': 1.0, 'longitude': 1.0, 'capacity': 1}]
        with patch('swagger_server.repositories.event_repository.db.session.query') as mock_query:
            mock_query.return_value.all.return_value = event_data
            events = self.event_repository.get_events()
        mock_query.assert_called_once_with(EventModel)
        
if __name__ == '__main__':
    unittest.main()
