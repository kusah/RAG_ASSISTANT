from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.crud.user import (
    create_user,
    get_user_by_email,
    get_user_by_username,
)

from app.schemas.user import UserLogin, Token
from app.crud.user import authenticate_user
from app.auth.jwt_handler import create_access_token



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):

    if get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    if get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    return create_user(db, user)


@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):

    authenticated_user = authenticate_user(
        db,
        user.email,
        user.password
    )

    if not authenticated_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {
            "sub": authenticated_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }