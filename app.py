"""Application that maps contacts to applications used to message them."""

import kivy

from conmap_app import ConmapApp

kivy.require("2.0.0")


def main() -> None:
    """Entry point for script."""
    app = ConmapApp()
    app.run()
    return


if __name__ == "__main__":
    main()
