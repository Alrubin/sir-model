from dash import html
import dash_bootstrap_components as dbc


class EvolutionPanel:
    def __call__(self):
        graph_scenario = dbc.CardBody([
            self.title_row(),
            html.Hr(),
            html.Div(id="scenario_content")
        ])

        return html.Div(dbc.Card(children=[graph_scenario],
                                 color="secondary",
                                 outline=True),
                        id="pagecontent",
                        style={
                            "margin-left": "25rem",
                            "margin-right": "0rem",
                            "padding": "2rem 1rem",
                            }
                        )

    def title_row(self):
        return dbc.Row([dbc.Col(self.title(), width=9)
                        ])

    def title(self):
        return html.H4("Evoluzione temporale dell'epidemia")
