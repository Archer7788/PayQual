from fastapi import Header

from app.database.database import SessionLocal

from app.models.user_model import User

from app.auth.security import (
    decode_access_token
)


def get_current_user(
    authorization: str = Header(None)
):

    if not authorization:

        return None

    token = authorization.replace(
        "Bearer ",
        ""
    )

    payload = decode_access_token(
        token
    )

    if not payload:

        return None

    username = payload.get("sub")

    db = SessionLocal()

    user = (
        db.query(User)
        .filter(
            User.username == username
        )
        .first()
    )

    db.close()

    return user