from pydantic import BaseModel

class IssueCreate(BaseModel):
    title: str
    description: str | None = None

class IssueResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str

    model_config = {
        "from_attributes": True
    }