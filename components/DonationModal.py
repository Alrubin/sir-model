from dash_bootstrap_components import Modal, ModalHeader, ModalTitle, ModalBody, ModalFooter, Button


class DonationModal(Modal):

    def __init__(self, paypal: str, text: str):
        self.paypal = paypal
        self.text = text

        super().__init__(children=self.build_modal(),
                         id="donation_modal",
                         is_open=False,
                         size="lg")

    def build_modal(self):
        header = ModalHeader(ModalTitle("Donazione"))
        body = ModalBody(self.text)
        footer = ModalFooter(self.paypal_button())
        return [header, body, footer]

    def paypal_button(self):
        return Button(children="Paypal",
                      id="paypal",
                      className="ml-auto",
                      color="warning",
                      href=self.paypal)
