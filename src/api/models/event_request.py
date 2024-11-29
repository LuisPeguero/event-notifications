from pydantic import BaseModel, Field

class EventRequest(BaseModel):
    user_id: str = Field(..., description="User ID")
    description: str = Field(..., description="Event description")
