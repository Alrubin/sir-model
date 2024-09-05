from dash.html import Div
from components.DonationModal import DonationModal
from components.ControlPanel import ControlPanel
from components.CentralBar import CentralBar
from components.GraphCard import GraphCard
from components.LeftSidebar import LeftSidebar
from components.NavBar import NavBar
from components.MainGraph import MainGraph
from lib.population import InitialValues
from lib.scenario import SIRScenario
from dash import callback, Output, Input


class AppLayout(Div):
    def __init__(self):
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

        super().__init__(children=[
            NavBar(repository_url="https://github.com/Alrubin/sir-model",
                   donation_modal=self.donation_modal()),
            LeftSidebar([ControlPanel()]),
            CentralBar([self.graph_card()])
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
