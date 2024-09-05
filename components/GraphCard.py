from dash.html import H4, Div, Hr, P
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Row, Col, Card, CardBody


class GraphCard(Card):

    def __init__(self, title, footer_description, central_graph):
        self.title = title
        self.footer_description = footer_description
        self.central_graph = central_graph

        super().__init__(
            children=self.children(),
            color="secondary",
            outline=True
        )

    def children(self):
        return CardBody([
            self.title_row(),
            Hr(),
            self.central_graph,
            P(),
            self.footer()
        ])

    def title_row(self):
        return Row([Col(H4(self.title), width=9)])

    def footer(self):
        return Row([
            Col(H4(" "), width=2),
            Col(H4(self.footer_description), width=6),
            Col(dbc.Input(id="giorni", type="number", value=120), width=3),
            Col(H4(" "), width=1)
        ])
