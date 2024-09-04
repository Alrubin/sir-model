from dash_bootstrap_components import Modal, ModalHeader, ModalTitle, ModalBody, ModalFooter, Button


class DonationModal(Modal):

    def __init__(self, paypal_link: str, message: str, title: str):
        self.paypal_link = paypal_link
        self.message = message
        self.title = title

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
            id="paypal",
            className="ml-auto",
            color="warning",
            href=self.paypal_link
        )
