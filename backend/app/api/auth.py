from fastapi import APIRouter

from pydantic import BaseModel

from app.database.database import SessionLocal

from app.models.user_model import User
from pydantic import BaseModel, Field

from app.auth.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()


class RegisterRequest(BaseModel):

    username: str

    password: str = Field(
    min_length=6,
    max_length=32
)


class LoginRequest(BaseModel):

    username: str

    password: str


@router.post("/register")
def register(data: RegisterRequest):

    db = SessionLocal()

    existing_user = (
        db.query(User)
        .filter(
            User.username == data.username
        )
        .first()
    )

    if existing_user:

        db.close()

        return {
            "error": "Username already exists"
        }

    hashed_password = hash_password(
        data.password
    )

    new_user = User(
        username=data.username,
        password=hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    db.close()

    return {
        "message":
            "User registered successfully"
    }


@router.post("/login")
def login(data: LoginRequest):

    db = SessionLocal()

    user = (
        db.query(User)
        .filter(
            User.username == data.username
        )
        .first()
    )

    db.close()

    if not user:

        return {
            "error": "Invalid username"
        }

    if not verify_password(
        data.password,
        user.password
    ):

        return {
            "error": "Invalid password"
        }

    access_token = create_access_token(
        data={
            "sub": user.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }