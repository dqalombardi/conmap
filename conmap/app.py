"""Application that maps contacts to applications used to message them."""

import kivy

from conmap.conmap_app import ConmapApp
from conmap.logging import get_logger

kivy.require("2.0.0")

logger = get_logger(__name__)


def main() -> None:
    """Entry point for script."""
    app = ConmapApp()
    logger.debug("Running ConmapApp")
    app.run()
    return


if __name__ == "__main__":
    main()
