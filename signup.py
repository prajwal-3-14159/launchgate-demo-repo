"""Sign-up flow."""
import uuid

from analytics import track

USERS: dict[str, dict] = {}


def create_user(email: str, password_hash: str, latitude: float, longitude: float) -> dict:
    user = {
        "id": str(uuid.uuid4()),
        "email": email,
        "password_hash": password_hash,
        "home_location": {"lat": latitude, "lon": longitude},
    }
    USERS[user["id"]] = user
    track("signup_completed", user)
    return user
