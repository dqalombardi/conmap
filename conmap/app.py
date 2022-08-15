"""Application that maps contacts to applications used to message them."""

import kivy
from conmap.conmap_app import ConmapApp
from conmap.constants import PIXEL_4A_RATIO
from conmap.logging import get_logger
from kivy.core.window import Window


kivy.require("2.0.0")
TEST_WIDTH = 300
Window.size = (TEST_WIDTH, int(PIXEL_4A_RATIO * TEST_WIDTH))


logger = get_logger(__name__)


def main() -> None:
    """Entry point for script."""
    app = ConmapApp()
    logger.debug("Running ConmapApp")
    app.run()
    return


if __name__ == "__main__":
    main()
