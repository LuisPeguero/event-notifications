from api.models.event import Event
from logger import logger

class NotificationService:
    @staticmethod
    def send_email(event: Event):
        print(f"Event {event.event_id} has been sent to {event.user_id}: {event.description}")
        logger.info(f"Email has been sent to {event.user_id}")

    @staticmethod
    def send_sms(event: Event):
        print(f"Event {event.event_id} has been sent to {event.user_id}: {event.description}")
        logger.info(f"SMS has been sent to {event.user_id}")

    @staticmethod
    def send_push_notification(event: Event):
        print(f"Event {event.event_id} has been sent to {event.user_id}: {event.description}")
        logger.info(f"Push notification has been sent to {event.user_id}")

    @staticmethod
    def send_all_channels(event: Event):
        logger.info(f"Sending notification to all channels for event {event.event_id}")
        NotificationService.send_email(event)
        NotificationService.send_sms(event)
        NotificationService.send_push_notification(event)