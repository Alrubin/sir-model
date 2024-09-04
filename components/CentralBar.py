from dash.html import Div, P, Hr, H4
from dash_bootstrap_components import CardBody, Card, Row, Col, Input


class CentralBar(Div):
    layout = {
        "margin-left": "25rem",
        "margin-right": "0rem",
        "padding": "2rem 1rem",
    }

    def __init__(self, children: list):
        self.children = children
        super().__init__(children=self.children, style=self.layout)
