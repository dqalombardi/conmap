"""Module containing package constants."""

import json

from constants import CONTACT_TO_APP_JSON
from messaging_app import MessagingApp

from .types import ContactToAppMap


def load_contact_to_app() -> ContactToAppMap:
    """Loads map from JSON file."""

    if not CONTACT_TO_APP_JSON.is_file():
        return {}

    file_content = CONTACT_TO_APP_JSON.read_text(encoding="utf8")
    raw_contact_to_app = json.loads(file_content)
    contact_to_app = {contact: MessagingApp.from_value(app_str) for contact, app_str in raw_contact_to_app.items()}

    return contact_to_app


def dump_contact_to_app(contact_to_app: ContactToAppMap) -> None:
    """Dumps map to JSON file."""

    # Serialising map
    json_serialised_contact_to_app = {contact: str(app) for contact, app in contact_to_app.items()}

    # Dumping map
    CONTACT_TO_APP_JSON.write_text(
        data=json.dumps(json_serialised_contact_to_app, indent=4, sort_keys=True, ensure_ascii=False),
        encoding="utf8",
    )

    return


def add_to_contact_to_app(contact: str, app: MessagingApp, overwrite: bool = False) -> None:
    """
    Adds passed contact-map pair to map.
    Raises ValueError if passed contact already in map and `overwrite` not passed.
    """

    # Loading map
    contact_to_app = load_contact_to_app()

    # Raising ValueError if passed contact already in map and `overwrite` not passed.
    if not overwrite and contact in contact_to_app:
        raise ValueError(
            f"Cannot add contact '{contact}' to map because they are already mapped to '{contact_to_app[app]}'; "
            "pass `overwrite=True` if you want to enable overwriting"
        )

    # Adding contact to map
    contact_to_app[contact] = app

    # Saving map
    dump_contact_to_app(contact_to_app)

    return
