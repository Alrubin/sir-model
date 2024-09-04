from dash_bootstrap_components import Modal, ModalHeader, ModalTitle, ModalBody, ModalFooter, Button
from dash import callback, Output, Input, State


class DonationModal(Modal):

    def __init__(self, paypal_link: str, message: str, title: str):
        self.paypal_link = paypal_link
        self.message = message
        self.title = title

        @callback(
            Output(component_id="donation_modal", component_property="is_open"),
            Input(component_id="donation_button", component_property="n_clicks"),
            State(component_id="donation_modal", component_property="is_open"),
        )
        def trigger(n_clicks, is_open):
            return not is_open if n_clicks else is_open

        super().__init__(
            children=self.children(),
            id="donation_modal",
            is_open=False,
            size="lg"
        )

    def children(self):
        header = ModalHeader(ModalTitle(self.title))
        body = ModalBody(self.message)
        footer = ModalFooter(self.paypal_button())
        return [header, body, footer]

    def paypal_button(self):
        return Button(
            children="Paypal",
            className="ml-auto",
            color="warning",
            href=self.paypal_link
        )
