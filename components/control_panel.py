import dash_bootstrap_components as dbc
from dash import html, dcc


class ControlPanel:

    def __call__(self):

        return html.Div(children=self.initial_conditions_panel())


    def initial_conditions_panel(self):
        return dbc.Col(children=[
            self.initial_condition(field="Susceptibles", input_id="S0",initial_value=100),
            self.initial_condition(field="Infected", input_id="I0", initial_value=0),
            self.initial_condition(field="Removed", input_id="R0", initial_value=0),
        ])

    def initial_condition(self, field: str, input_id: str, initial_value: int):
        return dbc.Row(children=[
                    dbc.Label(children=f"{field}:", width=7),
                    dbc.Col(dbc.Input(id=input_id, type="number", value=initial_value, size="sm"), width=5)
                    ], class_name="mb-3")
