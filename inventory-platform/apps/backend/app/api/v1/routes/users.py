from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import hash_password
from app.db.session import get_db
from app.db import models
from app.schemas import user as user_schema

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    new_user = models.User(
        email=user.email,
        hashed_password=hash_password(user.password)

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", response_model=list[user_schema.User])
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
