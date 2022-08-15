"""Module containing package constants."""

import json

from conmap.constants import CONTACT_TO_APP_JSON
from conmap.logging import get_logger
from conmap.messaging_app import MessagingApp
from conmap.types import ContactToAppMap

logger = get_logger(__name__)


def load_contact_to_app() -> ContactToAppMap:
    """Loads map from JSON file."""

    logger.debug(f"Loading map from file {CONTACT_TO_APP_JSON}")

    if not CONTACT_TO_APP_JSON.is_file():
        logger.debug(f"File does not exist; returning empty map - {CONTACT_TO_APP_JSON}")
        return {}

    file_content = CONTACT_TO_APP_JSON.read_text(encoding="utf8")
    raw_contact_to_app = json.loads(file_content)
    contact_to_app = {contact: MessagingApp.from_value(app_str) for contact, app_str in raw_contact_to_app.items()}

    return contact_to_app


def dump_contact_to_app(contact_to_app: ContactToAppMap) -> None:
    """Dumps map to JSON file."""

    logger.debug(f"Dumping map to file {CONTACT_TO_APP_JSON}")

    # Serialising map
    json_serialised_contact_to_app = {
        contact: str(contact_to_app[contact]) for contact in sorted(contact_to_app.keys())
    }

    # Dumping map
    parent = CONTACT_TO_APP_JSON.parent
    parent.mkdir(parents=True, exist_ok=True)
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

    logger.debug(f"Adding to map: {contact} -> {app}")

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
