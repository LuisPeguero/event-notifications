import pytest
from api.models.event import Event
from api.services.notifications import NotificationService

@pytest.fixture
def sample_event():
    return Event(user_id="user1", description="Sample Event")

def test_send_email(sample_event, mocker):
    mock_logger = mocker.patch("api.services.notifications.logger")
    NotificationService.send_email(sample_event)
    mock_logger.info.assert_called_once_with(f"Email has been sent to {sample_event.user_id}")

def test_send_sms(sample_event, mocker):
    mock_logger = mocker.patch("api.services.notifications.logger")
    NotificationService.send_sms(sample_event)
    mock_logger.info.assert_called_once_with(f"SMS has been sent to {sample_event.user_id}")

def test_send_push_notification(sample_event, mocker):
    mock_logger = mocker.patch("api.services.notifications.logger")
    NotificationService.send_push_notification(sample_event)
    mock_logger.info.assert_called_once_with(f"Push notification has been sent to {sample_event.user_id}")

def test_send_all_channels(sample_event, mocker):
    mock_send_email = mocker.patch.object(NotificationService, 'send_email')
    mock_send_sms = mocker.patch.object(NotificationService, 'send_sms')
    mock_send_push_notification = mocker.patch.object(NotificationService, 'send_push_notification')
    mock_logger = mocker.patch("api.services.notifications.logger")

    NotificationService.send_all_channels(sample_event)

    mock_logger.info.assert_any_call(f"Sending notification to all channels for event {sample_event.event_id}")
    mock_send_email.assert_called_once_with(sample_event)
    mock_send_sms.assert_called_once_with(sample_event)
    mock_send_push_notification.assert_called_once_with(sample_event)
