import dash_bootstrap_components as dbc
from dash import html


class Navbar(dbc.NavbarSimple):

    def __init__(self, github: str):
        self.github = github

        donation_button_with_modal = html.Div([
            self.donation_button(),
            DonationModal(paypal='https://paypal.me/alessandrorubin1'),
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


class DonationModal(dbc.Modal):

    def __init__(self, paypal: str):
        self.paypal = paypal

        header = dbc.ModalHeader(dbc.ModalTitle("Donazione"))
        body = dbc.ModalBody("""L'accesso a questa dashboard è gratuito perchè sono profondamente convinto che la cultura non abbia prezzo.
                            Tuttavia, sviluppare e mantenere il codice per garantire un servizio sempre aggiornato è un lavoro importante. 
                            Se hai apprezzato questo strumento, considera una donazione per supportarmi.""")
        button = dbc.Button(children="Paypal",
                            id="paypal",
                            className="ml-auto",
                            color="warning",
                            href=self.paypal)
        footer = dbc.ModalFooter(button)

        super().__init__(children=[
            header, body, footer
        ], id="donation_modal", is_open=False, size="lg")


def trigger_donation_modal(n_clicks, is_open):
    return not is_open if n_clicks else is_open
