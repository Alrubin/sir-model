from dash.html import Div
from components.DonationModal import DonationModal
from components.ControlPanel import ControlPanel
from components.EvolutionPanel import EvolutionPanel
from components.NavBar import NavBar


class AppLayout(Div):
    def __init__(self):
        super().__init__(children=[
            self.navbar(),
            self.left_sidebar(),
            EvolutionPanel("Evoluzione temporale dell'epidemia")
        ])

    def navbar(self):
        donation_modal = DonationModal(
            paypal='https://paypal.me/alessandrorubin1',
            text="L'accesso a questa dashboard è gratuito perchè sono profondamente convinto che la cultura non abbia prezzo." \
                 "Tuttavia, sviluppare e mantenere il codice per garantire un servizio sempre aggiornato è un lavoro importante." \
                 "Se hai apprezzato questo strumento, considera una donazione per supportarmi.""")
        return NavBar(github="https://github.com/Alrubin/sir-model",
                      donation_modal=donation_modal)

    def left_sidebar(self):
        return Div(children=[ControlPanel()], style={
            "position": "fixed",
            "top": 62.5,
            "left": 0,
            "bottom": 0,
            "width": "24rem",
            "height": "100%",
            "z-index": 1,
            "overflow-x": "hidden",
            "transition": "all 0.5s",
            "padding": "2rem 1rem",
            "background-color": "#f8f9fa",
        })
