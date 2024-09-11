import dash
from dash_bootstrap_components import Row, Label, Col, Accordion, AccordionItem, Input, Button
from dash.html import Div

from lib.population import InitialValues


class ControlPanel(Div):

    def __init__(self):
        @dash.callback(
            dash.Output("S0", "children"),
            [dash.Input(component_id='N0', component_property='value'),
             dash.Input(component_id='I0', component_property='value'),
             dash.Input(component_id='R0', component_property='value')
             ])
        def initial_susceptibles(N, I0, R0):
            initial_values = InitialValues(population=N, infected=I0, removed=R0)
            return f"Suscettibili: {initial_values.susceptibles}"

        accordion = Accordion(children=[
            AccordionItem(children=[self.initial_conditions_panel()], title="Condizioni demografiche iniziali"),
            AccordionItem(children=[self.disease_properties_panel()], title="Caratteristiche del patogeno")
        ], start_collapsed=True)

        super().__init__(children=accordion)

    def initial_conditions_panel(self):
        return Col(children=[
            self.initial_condition(field="Popolazione", input_id="N0", initial_value=90000, min=0, step=1),
            self.initial_condition(field="Infetti", input_id="I0", initial_value=0, min=0, step=1),
            self.initial_condition(field="Rimossi", input_id="R0", initial_value=0, min=0, step=1),
            Col(Button(id="S0", color="light", class_name="d-grid gap-2 col-12 mx-auto")),
        ])

    def disease_properties_panel(self):
        return Col(children=[
            self.initial_condition(field="Transmission rate", input_id="tr", initial_value=0.1, min=0, step=0.05),
            self.initial_condition(field="Recovery rate", input_id="rr", initial_value=0.1, min=0, step=0.05)
        ])

    def initial_condition(self, field: str, input_id: str, initial_value: float, min: float, step: float):
        return Row(children=[
            Label(children=f"{field}:", width=7),
            Col(Input(id=input_id, type="number", value=initial_value, size="sm", min=min, step=step), width=5)
        ], class_name="mb-3")
