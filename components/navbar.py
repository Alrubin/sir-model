import dash_bootstrap_components as dbc
from dash import html


class Navbar:

    def __call__(self):
        donation_button_with_modal = html.Div([
            self.donation_button(),
            self.donation_modal(),
        ])

        navigation_links = dbc.Nav([self.github_link(),
                                    donation_button_with_modal
                                    ])

        return dbc.NavbarSimple(
            children=[navigation_links],
            brand="SIRModel",
            color="dark",
            dark=True,
        )

    def github_link(self):
        return dbc.NavItem(dbc.NavLink(children="Github", href="https://github.com/Alrubin/sir-model"))

    def donation_button(self):
        return dbc.Button(children="Donate", id="donation_button", n_clicks=0, class_name="me-1", color="warning")

    def donation_modal(self):
        header = dbc.ModalHeader(dbc.ModalTitle("Donazione"))
        body = dbc.ModalBody("""L'accesso a questa dashboard è gratuito perchè sono profondamente convinto che la cultura non abbia prezzo.
                            Tuttavia, sviluppare e mantenere il codice per garantire un servizio sempre aggiornato è un lavoro importante. 
                            Se hai apprezzato questo strumento, considera una donazione per supportarmi.""")
        footer = dbc.ModalFooter(dbc.Button(children="Paypal",
                                            id="paypal",
                                            className="ml-auto",
                                            color="warning",
                                            href='https://paypal.me/alessandrorubin1')
                                 )
        return dbc.Modal(children=[
            header, body, footer
        ], id="donation_modal", is_open=False, size="lg")


def trigger_donation_modal(n_clicks, is_open):
    return not is_open if n_clicks else is_open
