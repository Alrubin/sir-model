from dash.html import Div
from components.DonationModal import DonationModal
from components.ControlPanel import ControlPanel
from components.EvolutionPanel import EvolutionPanel
from components.LeftSidebar import LeftSidebar
from components.NavBar import NavBar


class AppLayout(Div):
    def __init__(self):
        self.donation_modal = DonationModal(
            paypal='https://paypal.me/alessandrorubin1',
            text="L'accesso a questa dashboard è gratuito perchè sono profondamente convinto che la cultura non abbia prezzo." \
                 "Tuttavia, sviluppare e mantenere il codice per garantire un servizio sempre aggiornato è un lavoro importante." \
                 "Se hai apprezzato questo strumento, considera una donazione per supportarmi.""")
        super().__init__(children=[
            NavBar(github="https://github.com/Alrubin/sir-model",
                   donation_modal=self.donation_modal),
            LeftSidebar([ControlPanel()]),
            EvolutionPanel("Evoluzione temporale dell'epidemia")
        ])
