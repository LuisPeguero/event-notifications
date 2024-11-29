from typing import List

from api.models.event import Event
from api.models.event_request import EventRequest
from api.models.update_event_request import EventUpdateRequest
from fastapi import APIRouter, HTTPException
from notification_processor import process_event

router = APIRouter()

# In-memory store for events
events_store: List[Event] = []

@router.get("/events", response_model=List[Event])
async def get_event():
    """
    Retrieve all events.

    Returns:
        List[Event]: A list of all events.

    Raises:
        HTTPException: If the events list is empty.
    """
    if not events_store:
        raise HTTPException(status_code=404, detail="Events list empty")
    return events_store

@router.get("/events/{event_id}", response_model=Event)
async def get_event(event_id: str):
    """
    Retrieve a specific event by its ID.

    Args:
        event_id (str): The ID of the event to retrieve.

    Returns:
        Event: The event with the specified ID.

    Raises:
        HTTPException: If the event is not found.
    """
    event = next((event for event in events_store if event.event_id == event_id), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.post("/events", response_model=Event)
async def create_event(request: EventRequest):
    """
    Create a new event.

    Args:
        request (EventRequest): The request body containing the event details.

    Returns:
        Event: The created event.
    """
    event = Event(
        user_id=request.user_id,
        description=request.description
    )
    events_store.append(event)
    process_event.delay(event)
    return event

@router.put("/events/{event_id}", response_model=Event)
async def update_event(event_id: str, request: EventUpdateRequest):
    """
    Update an existing event's status.

    Args:
        event_id (str): The ID of the event to update.
        request (EventUpdateRequest): The request body containing the updated status.

    Returns:
        Event: The updated event.

    Raises:
        HTTPException: If the event is not found.
    """
    event = next((event for event in events_store if event.event_id == event_id), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    event.status = request.status
    return event


