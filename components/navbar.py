import dash_bootstrap_components as dbc
from dash import html

from components.DonationModal import DonationModal


class Navbar(dbc.NavbarSimple):

    def __init__(self, github: str):
        self.github = github

        donation_button_with_modal = html.Div([
            self.donation_button(),
            DonationModal(paypal='https://paypal.me/alessandrorubin1',
                          text="""L'accesso a questa dashboard è gratuito perchè sono profondamente convinto che la cultura non abbia prezzo.
                            Tuttavia, sviluppare e mantenere il codice per garantire un servizio sempre aggiornato è un lavoro importante. 
                            Se hai apprezzato questo strumento, considera una donazione per supportarmi."""),
        ])

        navigation_links = dbc.Nav([self.github_link(),
                                    donation_button_with_modal
                                    ])

        super().__init__(
            children=[navigation_links],
            brand="SIRModel",
            color="dark",
            dark=True,
        )

    def github_link(self):
        return dbc.NavItem(dbc.NavLink(children="Github", href=self.github))

    def donation_button(self):
        return dbc.Button(children="Donate", id="donation_button", n_clicks=0, class_name="me-1", color="warning")


def trigger_donation_modal(n_clicks: int, is_open: bool):
    return not is_open if n_clicks else is_open
