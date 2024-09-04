from dash_bootstrap_components import Modal, NavbarSimple, Nav, NavLink, NavItem, Button
from dash.html import Div


class NavBar(NavbarSimple):

    def __init__(self, repository_url: str, donation_modal: Modal):
        self.github = repository_url
        self.donation_modal = donation_modal
        self.navigation_links = Nav([self.github_link(), self.button_with_donation_modal()])

        super().__init__(
            children=[self.navigation_links],
            brand="SIRModel",
            color="dark",
            dark=True,
        )

    def button_with_donation_modal(self):
        return Div([
            self.donation_button(),
            self.donation_modal,
        ])

    def github_link(self):
        return NavItem(NavLink(children="Github", href=self.github))

    def donation_button(self):
        return Button(children="Donate", id="donation_button", n_clicks=0, class_name="me-1", color="warning")


def trigger_donation_modal(n_clicks: int, is_open: bool):
    return not is_open if n_clicks else is_open
