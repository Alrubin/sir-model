from dash import Dash, html
import dash_bootstrap_components as dbc
from config import AppConfig

def SIRModelDash():
    app = Dash(__name__,
               title="SIRModelDash",
               suppress_callback_exceptions=True,
               external_stylesheets=[dbc.themes.YETI]
               )

    app.layout = html.Div()

    return app

app = SIRModelDash()

if __name__ == '__main__':
    app.run_server(debug=AppConfig.debug,
                   host=AppConfig.host,
                   port=AppConfig.port)