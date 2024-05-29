from dash import html
from components.navbar import Navbar


class AppLayout:
    def __call__(self):
        return html.Div([
            self.navbar()
            ])

    def navbar(self):
        return Navbar()()
