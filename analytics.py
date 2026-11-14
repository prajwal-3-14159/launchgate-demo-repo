"""Product analytics. Events go to MetricFlow (hosted in the United States)."""
import os

import requests

from config import ANALYTICS_ENDPOINT, ANALYTICS_WRITE_KEY_ENV


def track(event: str, user: dict) -> None:
    payload = {
        "event": event,
        "email": user["email"],
        "user_id": user["id"],
        "locale": user.get("locale", "ja-JP"),
    }
    requests.post(
        ANALYTICS_ENDPOINT,
        json=payload,
        headers={"Authorization": os.environ.get(ANALYTICS_WRITE_KEY_ENV, "")},
        timeout=5,
    )
