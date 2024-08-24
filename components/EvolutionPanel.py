from dash.html import Div, P, Hr, H4
from dash_bootstrap_components import CardBody, Card, Row, Col, Input


class EvolutionPanel(Div):
    def __init__(self, title: str):
        self.title = title

        graph_scenario = CardBody([
            self.title_row(),
            Hr(),
            Div(id="scenario_content"),
            P(),
            self.footer()
        ])

        super().__init__(
            children=Card(
                children=[graph_scenario],
                color="secondary",
                outline=True
            ),
            style={
                "margin-left": "25rem",
                "margin-right": "0rem",
                "padding": "2rem 1rem",
            })

    def title_row(self):
        return Row([Col(H4(self.title), width=9)])

    def footer(self):
        return Row([
            Col(H4(" "), width=2),
            Col(H4("Asse orizzontale (Giorni):"), width=6),
            Col(Input(id="giorni", type="number", value=120), width=3),
            Col(H4(" "), width=1)
        ])
