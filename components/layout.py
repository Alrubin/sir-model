from dash import html
from components.navbar import Navbar


class AppLayout:
    def __call__(self):
        navbar = Navbar()
        return html.Div([navbar()])
