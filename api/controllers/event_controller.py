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
    if not events_store:
        raise HTTPException(status_code=404, detail="Events list empty")
    return events_store

@router.get("/events/{event_id}", response_model=Event)
async def get_event(event_id: str):
    event = next((event for event in events_store if event.event_id == event_id), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.post("/events", response_model=Event)
async def create_event(request: EventRequest):
    event = Event(
        user_id=request.user_id,
        description=request.description
    )
    events_store.append(event)
    process_event.delay(event)
    return event

@router.put("/events/{event_id}", response_model=Event)
async def update_event(event_id: str, request: EventUpdateRequest):
    event = next((event for event in events_store if event.event_id == event_id), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    event.status = request.status
    return event


