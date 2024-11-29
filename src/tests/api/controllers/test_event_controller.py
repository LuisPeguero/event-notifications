import pytest
from fastapi.testclient import TestClient
from api.controllers.event_controller import router, events_store
from api.models.event import Event
from app import app

client = TestClient(app)
app.include_router(router)

@pytest.fixture
def setup_events():
    # Setup initial events
    event1 = Event(user_id="user1", description="Event 1")
    event2 = Event(user_id="user2", description="Event 2")
    events_store.extend([event1, event2])
    yield
    events_store.clear()

@pytest.fixture(autouse=True)
def mock_redis(mocker):
    mock_process = mocker.patch("api.controllers.event_controller.process_event")
    return mock_process

def test_get_events_empty():
    response = client.get("/events")
    assert response.status_code == 404
    assert response.json() == {"detail": "Events list empty"}

def test_get_events(setup_events):
    response = client.get("/events")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_event_not_found():
    response = client.get("/events/123134-fwef323-1321")
    assert response.status_code == 404
    assert response.json() == {"detail": "Event not found"}

def test_get_event(setup_events):
    event_id = events_store[0].event_id
    response = client.get(f"/events/{event_id}")
    assert response.status_code == 200
    assert response.json()["event_id"] == event_id

def test_create_event():
    request_data = {"user_id": "user3", "description": "Event 3"}
    response = client.post("/events", json=request_data)
    assert response.status_code == 200
    assert response.json()["user_id"] == "user3"
    assert response.json()["description"] == "Event 3"

def test_update_event_not_found():
    request_data = {"status": "completed"}
    response = client.put("/events/11111-22223-444-111", json=request_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Event not found"}

def test_update_event(setup_events):
    event_id = events_store[0].event_id
    request_data = {"status": "completed"}
    response = client.put(f"/events/{event_id}", json=request_data)
    assert response.status_code == 200
    assert response.json()["status"] == "completed"
