from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine
from app.deps import get_db
from app.models import Issue
from app.schemas import IssueCreate, IssueResponse
from fastapi import HTTPException

app = FastAPI(title="Issue Management System")

@app.get("/")
def root():
    return {"message": "Issue Management System API is running"}


@app.post("/issues", response_model=IssueResponse)
def create_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    new_issue = Issue(
        title=issue.title,
        description=issue.description
    )
    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    return new_issue

@app.get("/issues/{issue_id}", response_model=IssueResponse)
def get_issue(issue_id: int, db: Session = Depends(get_db)):
    issue = db.query(Issue).filter(Issue.id == issue_id).first()

    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")

    return issue
