from dash import Dash
from dash_bootstrap_components.themes import YETI
from components.AppLayout import AppLayout
import yaml


class Dashboard(Dash):
    def __init__(self, title, theme, layout):
        super().__init__(
            __name__,
            title=title,
            suppress_callback_exceptions=True,
            external_stylesheets=[theme]
        )
        self.layout = layout


if __name__ == '__main__':
    with open("config.yml", "r") as ymlfile:
        config = yaml.safe_load(ymlfile)

    app = Dashboard(
        title="SIRModelDash",
        theme=YETI,
        layout=AppLayout()
    )
    app.run_server(**config["server"])
