import uuid
from pydantic import BaseModel, PrivateAttr
from pydantic.fields import Field

class Event(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    description: str
    status: str = Field(default="created")

