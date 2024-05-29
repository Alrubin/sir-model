from dash import Output, Input, State
from components.navbar import trigger_donation_modal
from lib.scenario import update_scenario


def register_callbacks(app):
    app.callback(
        Output(component_id="donation_modal", component_property="is_open"),
        Input(component_id="donation_button", component_property="n_clicks"),
        State(component_id="donation_modal", component_property="is_open"),
    )(trigger_donation_modal)

    app.callback(
        Output(component_id="scenario_content", component_property="children"),
        Input(component_id='giorni', component_property='value')
    )(update_scenario)
