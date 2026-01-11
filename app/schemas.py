from pydantic import BaseModel
from datetime import datetime

class IssueCreate(BaseModel):
    title: str
    description: str | None = None
    status: str | None = None
    priority: str | None = None
    assigned_to: int | None = None


class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    model_config = {
        "from_attributes": True
    }


class IssueResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    priority: str
    version: int
    created_at: datetime
    assignee: UserResponse | None = None

    model_config = {
        "from_attributes": True
    }

class IssueUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    priority: str | None = None
    assigned_to: int | None = None
    version: int


