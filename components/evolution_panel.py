from dash import html
import dash_bootstrap_components as dbc


class EvolutionPanel:
    def __call__(self):
        graph_scenario = dbc.CardBody([
            self.title_row(),
            html.Hr(),
            html.Div(id="scenario_content"),
            html.P(),
            self.footer()
        ])

        return html.Div(
            dbc.Card(
                children=[graph_scenario],
                color="secondary",
                outline=True
            ),
            style={
                "margin-left": "25rem",
                "margin-right": "0rem",
                "padding": "2rem 1rem",
            }
        )

    def title_row(self):
        return dbc.Row([dbc.Col(self.title(), width=9)])

    def title(self):
        return html.H4("Evoluzione temporale dell'epidemia")

    def footer(self):
        return dbc.Row([
            dbc.Col(html.H4(" "), width=2),
            dbc.Col(html.H4("Asse orizzontale (Giorni):"), width=6),
            dbc.Col(dbc.Input(id="giorni", type="number", value=120), width=3),
            dbc.Col(html.H4(" "), width=1)
        ])
