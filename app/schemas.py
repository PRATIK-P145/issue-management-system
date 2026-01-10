from pydantic import BaseModel
from datetime import datetime

class IssueCreate(BaseModel):
    title: str
    description: str | None = None

class IssueResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    priority: str | None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }