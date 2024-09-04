from dash import Output, Input
from lib.scenario import update_scenario


def register_callbacks(app):


    app.callback(
        Output(component_id="scenario_content", component_property="children"),
        [Input(component_id='S0', component_property='value'),
         Input(component_id='I0', component_property='value'),
         Input(component_id='R0', component_property='value'),
         Input(component_id='giorni', component_property='value')]
    )(update_scenario)
