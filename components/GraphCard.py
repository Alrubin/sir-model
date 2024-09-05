from dash import callback, Output, Input
from dash.html import H4, Div, Hr, P
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Row, Col, Card, CardBody
from plotly.graph_objs import Layout
from components.MainGraph import MainGraph
from lib.population import InitialValues
from lib.scenario import SIRScenario


class GraphCard(Card):

    def __init__(self, title, footer_description):
        self.title = title
        self.footer_description = footer_description

        @callback(
            Output(component_id="scenario_content", component_property="children"),
            [Input(component_id='S0', component_property='value'),
             Input(component_id='I0', component_property='value'),
             Input(component_id='R0', component_property='value'),
             Input(component_id='giorni', component_property='value')]
        )
        def update_graph(S0, I0, R0, n_days):
            initial_conditions = InitialValues(susceptibles=S0, infected=I0, removed=R0)
            scenario = SIRScenario(initial_conditions=initial_conditions, disease=None)
            population_evolution = scenario.compute_evolution(n_days)
            return MainGraph(population_evolution)

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
            Col(H4(self.footer_description), width=6),
            Col(dbc.Input(id="giorni", type="number", value=120), width=3),
            Col(H4(" "), width=1)
        ])
