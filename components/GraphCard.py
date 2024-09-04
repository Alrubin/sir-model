from dash.html import H4, Div, Hr, P
from dash_bootstrap_components import Row, Col, Card, CardBody, Input


class GraphCard(Card):

    def __init__(self, title, footer_description):
        self.title = title
        self.footer_description = footer_description

        super().__init__(
            children=self.children(),
            color="secondary",
            outline=True
        )

    def children(self):
        return CardBody([
            self.title_row(),
            Hr(),
            Div(id="scenario_content"),
            P(),
            self.footer()
        ])

    def title_row(self):
        return Row([Col(H4(self.title), width=9)])

    def footer(self):
        return Row([
            Col(H4(" "), width=2),
            Col(H4(self.footer_descriptionn), width=6),
            Col(Input(id="giorni", type="number", value=120), width=3),
            Col(H4(" "), width=1)
        ])
