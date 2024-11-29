from pydantic import BaseModel, Field

class EventUpdateRequest(BaseModel):
    status: str = Field(..., description="Event status")