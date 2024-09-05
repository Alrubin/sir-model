from dash.html import Div


class LeftSidebar(Div):
    def __init__(self, children: list):
        self.children = children
        super().__init__(children=self.children, className="left-sidebar")
