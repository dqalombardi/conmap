"""Module containing ConmapApp enum."""

from enum import Enum, unique


@unique
class MessagingApp(Enum):
    WHATSAPP = "whatsapp"
    TELEGRAM = "telegram"

    @classmethod
    def from_value(cls, value: str) -> "MessagingApp":
        """
        Returns member of cls with the passed value.
        Raises ValueError if no such member exists.
        """

        for member in cls:
            if member.value == value:
                return member

        raise ValueError(f"There is no member of {cls} with passed value: '{value}'")

    def __str__(self) -> str:
        return self.value
