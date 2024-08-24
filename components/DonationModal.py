from dash_bootstrap_components import Modal, ModalHeader, ModalTitle, ModalBody, ModalFooter, Button


class DonationModal(Modal):

    def __init__(self, paypal: str, text: str):
        self.paypal = paypal
        self.text = text

        header = ModalHeader(ModalTitle("Donazione"))
        body = ModalBody(self.text)
        footer = ModalFooter(self.paypal_button())

        super().__init__(children=[
            header, body, footer
        ], id="donation_modal", is_open=False, size="lg")

    def paypal_button(self):
        return Button(children="Paypal",
                      id="paypal",
                      className="ml-auto",
                      color="warning",
                      href=self.paypal)
