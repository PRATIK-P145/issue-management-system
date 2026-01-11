from fastapi import FastAPI, Depends,Query
from sqlalchemy.orm import Session

from app.database import Base, engine
from app.deps import get_db
from app.models import Issue
from app.schemas import IssueCreate, IssueResponse
from fastapi import HTTPException
from typing import Optional

from app.schemas import UserCreate, UserResponse
from app.crud import create_user, get_users
from app.models import User


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

@app.get("/issues")
def list_issues(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    status: Optional[str] = None,
    priority: Optional[str] = None,
    db: Session = Depends(get_db),
):
    offset = (page - 1) * limit

    query = db.query(Issue)

    # filters (only if provided)
    if status:
        query = query.filter(Issue.status == status)

    if priority:
        query = query.filter(Issue.priority == priority)

    total = query.count()

    issues = (
        query
        .order_by(Issue.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )

    pages = (total + limit - 1) // limit

    return {
        "data": issues,
        "meta": {
            "total": total,
            "page": page,
            "pages": pages,
        },
    }

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.name, user.email)


@app.get("/users", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)
