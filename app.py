"""Application that maps contacts to applications used to message them."""

import kivy
from kivy.uix.widget import Widget

kivy.require("2.0.0")

from conmap_app import ConmapApp

CONTACT_TO_APP = {}


def main() -> None:
    """Entry point for script."""
    app = ConmapApp()
    app.run()
    return


if __name__ == "__main__":
    main()
