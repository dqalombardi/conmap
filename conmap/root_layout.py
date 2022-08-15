"""Module containing RootLayout class."""

from typing import List

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from conmap.logging import get_logger
from conmap.utils import load_contact_to_app

logger = get_logger(__name__)


class RootLayout(BoxLayout):
    def __init__(self, **kwargs):

        logger.debug("Initialising RootLayout")

        super().__init__(orientation="vertical", **kwargs)

        # Loading map
        contact_to_app = load_contact_to_app()

        # Constructing labels
        logger.debug("Constructing labels")
        labels: List[Label] = []
        for contact, app in contact_to_app.items():
            label = Label(
                text=f"{contact} -> {app}",
                font_size=20,
            )
            labels.append(label)

        # Adding labels to view
        logger.debug(f"Adding {len(labels)} labels to view")
        for label in labels:
            logger.debug(f"Adding label with text '{label.text}'")
            self.add_widget(label)

        return
