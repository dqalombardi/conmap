"""Module containing ConmapApp class."""

from kivy.app import App

from conmap.logging import get_logger
from conmap.root_layout import RootLayout

logger = get_logger(__name__)


class ConmapApp(App):
    """App for configuring contact map."""

    def build(self) -> RootLayout:
        logger.debug("Building ConmapApp")
        return RootLayout()
