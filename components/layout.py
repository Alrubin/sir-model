from dash import html

from components.DonationModal import DonationModal
from components.control_panel import ControlPanel
from components.evolution_panel import EvolutionPanel
from components.NavBar import NavBar


class AppLayout:
    def __call__(self):
        return html.Div([
            self.navbar(),
            self.left_sidebar(),
            self.central_bar()
        ])

    def navbar(self):
        donation_modal = DonationModal(paypal='https://paypal.me/alessandrorubin1',
                      text="""L'accesso a questa dashboard è gratuito perchè sono profondamente convinto che la cultura non abbia prezzo.
                                    Tuttavia, sviluppare e mantenere il codice per garantire un servizio sempre aggiornato è un lavoro importante. 
                                    Se hai apprezzato questo strumento, considera una donazione per supportarmi.""")
        return NavBar(github="https://github.com/Alrubin/sir-model",
                      donation_modal=donation_modal)


    def left_sidebar(self):
        return html.Div(children=[self.control_panel()], style={
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

    def central_bar(self):
        return EvolutionPanel()()

    def control_panel(self):
        return ControlPanel()()
