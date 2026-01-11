from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import User


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
