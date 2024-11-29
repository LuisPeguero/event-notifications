import requests

from celery import Celery
from api.models.event import Event
from api.models.update_event_request import EventUpdateRequest
from settings import REDIS_HOST, REDIS_PORT
from settings import EVENT_SERVICE_URL
from api.services.notifications import NotificationService
from logger import logger

celery = Celery(__name__)
celery.conf.broker_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
celery.conf.result_backend = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
celery.conf.event_serializer = 'pickle'
celery.conf.task_serializer = 'pickle'
celery.conf.result_serializer = 'pickle'
celery.conf.accept_content = ['application/json', 'application/x-python-serialize']

@celery.task()
def process_event(event: Event):
    logger.info(f"Processing event {event.event_id}")
    NotificationService.send_all_channels(event)
    response = requests.put(
        f"{EVENT_SERVICE_URL}/api/events/{event.event_id}", 
        json=EventUpdateRequest(status="processed").dict()
        )
    if response.status_code != 200:
        logger.error(f"Failed to update event {event.event_id} status")
        return f"Failed to update event {event.event_id} status"

    return f"Event has been processed and updated: with status code {response.status_code}"