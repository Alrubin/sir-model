from dash.html import Div
from components.DonationModal import DonationModal
from components.ControlPanel import ControlPanel
from components.EvolutionPanel import EvolutionPanel
from components.LeftSidebar import LeftSidebar
from components.NavBar import NavBar


class AppLayout(Div):
    def __init__(self):
        self.donation_modal = DonationModal(
            paypal_link='https://paypal.me/alessandrorubin1',
            message="L'accesso a questa dashboard è gratuito perchè sono profondamente convinto che la cultura non abbia prezzo." \
                 "Tuttavia, sviluppare e mantenere il codice per garantire un servizio sempre aggiornato è un lavoro importante." \
                 "Se hai apprezzato questo strumento, considera una donazione per supportarmi.""",
            title="Donazione"
        )
        super().__init__(children=[
            NavBar(repository_url="https://github.com/Alrubin/sir-model",
                   donation_modal=self.donation_modal),
            LeftSidebar([ControlPanel()]),
            EvolutionPanel(title="Evoluzione temporale dell'epidemia")
        ])
