"""Module containing ConmapApp enum."""

from enum import Enum, unique


@unique
class MessagingApp(Enum):
    WHATSAPP = "whatsapp"
    TELEGRAM = "telegram"

    @classmethod
    def from_value(cls, value: str) -> "MessagingApp":
        """TODO"""

        for app in cls:
            if app.value == value:
                return app

        raise ValueError(f"There is no member of {cls} with passed value: '{value}'")

    def __str__(self) -> str:
        return self.value
