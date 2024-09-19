import dash
from dash.dcc import Location, Slider
from dash_bootstrap_components import Row, Label, Col, Accordion, AccordionItem, Input, Button, CardBody, Card, \
    CardHeader
from dash.html import Div, P, A

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

        @dash.callback(
            dash.Output('current-url', 'href'),
            dash.Input('reset-button', 'n_clicks')
        )
        def refresh_page(n_clicks):
            if n_clicks:
                return '/'
            return None

        card_header = CardHeader("Pannello di controllo")
        card_body = CardBody(children=[
            self.settings(),
            P(),
            self.reset_button(),
            Location(id='current-url', refresh=True)
        ])

        super().__init__(children=Card([card_header, card_body]))

    def settings(self):
        return Accordion(children=[
            AccordionItem(children=[self.initial_conditions_panel()], title="Condizioni demografiche iniziali"),
            AccordionItem(children=[self.disease_properties_panel()], title="Caratteristiche del patogeno")
        ], start_collapsed=True)

    def reset_button(self):
        return Row([
            Button("Resetta valori", color="warning", class_name="me-1", id="reset-button")
        ], class_name="mb-3", style={"width": "20rem", "margin": "auto"})

    def initial_conditions_panel(self):
        return Col(children=[
            self.initial_condition(field="Popolazione", input_id="N0", initial_value=90000, min=0, step=1),
            self.initial_condition(field="Infetti", input_id="I0", initial_value=0, min=0, step=1),
            self.initial_condition(field="Rimossi", input_id="R0", initial_value=0, min=0, step=1),
            Col(Button(id="S0", color="light", class_name="d-grid gap-2 col-12 mx-auto")),
        ])

    def disease_properties_panel(self):
        return Col(children=[
            Row(children=[
                Label(children="Tasso di contatto:", width=7),
                Col(Input(id="contact_rate", type="number", value=5, size="sm"), width=5)
            ], class_name="mb-3"),

            Row(children=[
                Label(children="Tasso di infezione:"),
                MySlider("infection_rate")
            ], class_name="mb-3"),

            Row(children=[
                Label(children="Tasso di recupero:"),
                MySlider("recovery_rate")
            ], class_name="mb-3"),

        ])

    def initial_condition(self, field: str, input_id: str, initial_value: float, min: float, step: float):
        return Row(children=[
            Label(children=f"{field}:", width=7),
            Col(Input(id=input_id, type="number", value=initial_value, size="sm", min=min, step=step), width=5)
        ], class_name="mb-3")


class MySlider(Slider):
    def __init__(self, id):
        self.id = id

        super().__init__(
            min=0,
            max=100,
            step=1,
            value=10,
            id=self.id,
            marks={0: '0%', 25: '25%', 50: '50%', 75: '75%', 100: '100%'}
        )
