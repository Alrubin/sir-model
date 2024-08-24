from dash.html import Div


class LeftSidebar(Div):
    layout = {
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
            }
    def __init__(self, childrens: list):
        self.childrens = childrens
        super().__init__(children=self.childrens, style=self.layout)