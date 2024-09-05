from dash.html import Div


class VerticalBar(Div):
    def __init__(self, children: list, class_name):
        self.children = children
        self.class_name = class_name
        super().__init__(children=self.children, className=self.class_name)