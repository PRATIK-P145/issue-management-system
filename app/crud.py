from sqlalchemy.orm import Session
from models import Issue, User
from schemas import IssueCreate
from fastapi import HTTPException


def create_issue(db: Session, issue: IssueCreate) -> Issue:
    if issue.assigned_to is not None:
        user = db.query(User).filter(User.id == issue.assigned_to).first()
        if not user:
            raise HTTPException(status_code=400, detail="Assigned user not found")

    new_issue = Issue(
        title=issue.title,
        description=issue.description,
        status=issue.status,
        priority=issue.priority,
        assigned_to=issue.assigned_to,
    )

    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    return new_issue


def get_issue_by_id(db: Session, issue_id: int) -> Issue:
    issue = db.query(Issue).filter(Issue.id == issue_id).first()
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issue


def list_issues(
    db: Session,
    page: int,
    limit: int,
    status: str | None = None,
    priority: str | None = None,
):
    offset = (page - 1) * limit

    query = db.query(Issue)

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

def create_user(db: Session, name: str, email: str):
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code=409, detail="Email already exists")

    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    return db.query(User).order_by(User.id).all()
