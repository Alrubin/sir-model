from dash.html import Div
from components.DonationModal import DonationModal
from components.ControlPanel import ControlPanel
from components import VerticalBar
from components.GraphCard import GraphCard
from components.NavBar import NavBar
from components.MainGraph import MainGraph
from lib.disease import build_disease
from lib.population import InitialValues
from lib.scenario import SIRScenario
from dash import callback, Output, Input


class AppLayout(Div):
    def __init__(self):
        @callback(
            Output(component_id="scenario_content", component_property="children"),
            [Input(component_id='N0', component_property='value'),
             Input(component_id='I0', component_property='value'),
             Input(component_id='R0', component_property='value'),
             Input(component_id='giorni', component_property='value'),
             Input(component_id='infection_rate', component_property='value'),
             Input(component_id='contact_rate', component_property='value'),
             Input(component_id='recovery_rate', component_property='value'),
             ]
        )
        def update_graph(N0, I0, R0, n_days, infection_rate, contact_rate, recovery_rate):
            initial_conditions = InitialValues(population=N0, infected=I0, removed=R0)
            transmission_rate = (infection_rate/100)*(contact_rate/N0)
            recovery_rate = recovery_rate/100
            disease = build_disease(transmission_rate, recovery_rate)
            scenario = SIRScenario(initial_conditions=initial_conditions, disease=disease)
            population_evolution = scenario.compute_evolution(n_days)
            return MainGraph(population_evolution)

        super().__init__(children=[
            NavBar(repository_url="https://github.com/Alrubin/sir-model",
                   donation_modal=self.donation_modal()),
            VerticalBar(children=[ControlPanel()], class_name="left-sidebar"),
            VerticalBar(children=[self.graph_card()], class_name="central-bar")
        ])

    def graph_card(self):
        return GraphCard(
            title="Evoluzione temporale dell'epidemia",
            footer_description="Asse orizzontale (Giorni):",
            central_graph=Div(id="scenario_content")
        )

    def donation_modal(self):
        return DonationModal(
            paypal_link='https://paypal.me/alessandrorubin1',
            message="L'accesso a questa dashboard è gratuito perchè sono profondamente convinto che la cultura non abbia prezzo." \
                    "Tuttavia, sviluppare e mantenere il codice per garantire un servizio sempre aggiornato è un lavoro importante." \
                    "Se hai apprezzato questo strumento, considera una donazione per supportarmi.""",
            title="Donazione"
        )
