from dash import Output, Input, State

from components.navbar import trigger_donation_modal


def register_callbacks(app):
    app.callback(
        Output("donation_modal", "is_open"),
        Input("donation_button", "n_clicks"),
        State("donation_modal", "is_open"),
    )(trigger_donation_modal)
