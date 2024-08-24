from dash import Dash
from dash_bootstrap_components.themes import YETI
from callbacks.callbacks import register_callbacks
from components.AppLayout import AppLayout
import yaml


class Dashboard(Dash):
    def __init__(self, title, theme, layout, callbacks):
        super().__init__(
            __name__,
            title=title,
            suppress_callback_exceptions=True,
            external_stylesheets=[theme]
        )
        self.layout = layout
        callbacks(self)


if __name__ == '__main__':
    with open("config.yml", "r") as ymlfile:
        config = yaml.safe_load(ymlfile)

    app = Dashboard(
        title="SIRModelDash",
        theme=YETI,
        layout=AppLayout(),
        callbacks=register_callbacks
    )
    app.run_server(**config["server"])
