from dash_bootstrap_components import Row, Label, Col, Accordion, AccordionItem, Input
from dash.html import Div


class ControlPanel(Div):

    def __init__(self):
        accordion = Accordion(children=[
            AccordionItem(children=[self.initial_conditions_panel()], title="Initial conditions")
        ], start_collapsed=True)

        super().__init__(children=accordion)

    def initial_conditions_panel(self):
        return Col(children=[
            self.initial_condition(field="Susceptibles", input_id="S0", initial_value=100),
            self.initial_condition(field="Infected", input_id="I0", initial_value=0),
            self.initial_condition(field="Removed", input_id="R0", initial_value=0),
        ])

    def initial_condition(self, field: str, input_id: str, initial_value: int):
        return Row(children=[
            Label(children=f"{field}:", width=7),
            Col(Input(id=input_id, type="number", value=initial_value, size="sm", min=0, step=1), width=5)
        ], class_name="mb-3")