import dash_bootstrap_components as dbc
from dash_bootstrap_components import Modal
from dash import html


class Navbar(dbc.NavbarSimple):

    def __init__(self, github: str, donation_modal: Modal):
        self.github = github
        self.donation_modal = donation_modal

        donation_button_with_modal = html.Div([
            self.donation_button(),
            self.donation_modal,
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
