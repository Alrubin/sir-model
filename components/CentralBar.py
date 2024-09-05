from dash.html import Div


class CentralBar(Div):
    def __init__(self, children: list):
        self.children = children
        super().__init__(children=self.children, className="central-bar")
