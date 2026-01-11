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
def create_issue_endpoint(issue: IssueCreate, db: Session = Depends(get_db)):
    return create_issue(db, issue)


@app.get("/issues/{issue_id}", response_model=IssueResponse)
def get_issue_endpoint(issue_id: int, db: Session = Depends(get_db)):
    return get_issue_by_id(db, issue_id)


@app.get("/issues")
def list_issues_endpoint(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    status: str | None = None,
    priority: str | None = None,
    db: Session = Depends(get_db),
):
    return list_issues(db, page, limit, status, priority)

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.name, user.email)


@app.get("/users", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)
