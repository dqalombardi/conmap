"""Module containing ConmapApp class."""

from kivy.app import App

from root_layout import RootLayout


class ConmapApp(App):
    """App for configuring contact map."""

    def build(self) -> RootLayout:
        return RootLayout()
