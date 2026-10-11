"""Lightweight input validation for the sample Book API.

OpenAPI schemas live in openapi.yaml. This module does not automatically
read or generate Python code from that specification.
"""

from flask import request


def parse_book_payload(required_fields):
    """Return (payload, error_message); validate a JSON object and fields."""
    if not request.is_json:
        return None, "Content-Type must be application/json"

    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return None, "Request body must be a JSON object"

    missing = [field for field in required_fields if field not in payload]
    if missing:
        return None, f"Missing required field(s): {', '.join(missing)}"

    title = payload.get("title")
    author = payload.get("author")
    year = payload.get("published_year")

    if "title" in required_fields and (
        not isinstance(title, str) or not title.strip()
    ):
        return None, "'title' must be a non-empty string"

    if "author" in required_fields and (
        not isinstance(author, str) or not author.strip()
    ):
        return None, "'author' must be a non-empty string"

    if "published_year" in required_fields:
        # bool is a subclass of int in Python, so reject it explicitly.
        if isinstance(year, bool) or not isinstance(year, int):
            return None, "'published_year' must be an integer"
        if year < 0:
            return None, "'published_year' must be greater than or equal to 0"

    return payload, None
