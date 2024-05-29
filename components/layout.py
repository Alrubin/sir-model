from dash import html
from components.evolution_panel import EvolutionPanel
from components.navbar import Navbar


class AppLayout:
    def __call__(self):
        return html.Div([
            self.navbar(),
            self.left_sidebar(),
            self.central_bar()
        ])

    def navbar(self):
        return Navbar()()

    def left_sidebar(self):
        return html.Div(children=[], style={
            "position": "fixed",
            "top": 62.5,
            "left": 0,
            "bottom": 0,
            "width": "24rem",
            "height": "100%",
            "z-index": 1,
            "overflow-x": "hidden",
            "transition": "all 0.5s",
            "padding": "2rem 1rem",
            "background-color": "#f8f9fa",
        })

    def central_bar(self):
        return EvolutionPanel()()
