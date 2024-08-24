from dash import Dash
from dash_bootstrap_components.themes import YETI
from callbacks.callbacks import register_callbacks
from components.AppLayout import AppLayout


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
    app = Dashboard(
        title="SIRModelDash",
        theme=YETI,
        layout=AppLayout(),
        callbacks=register_callbacks
    )
    app.run_server(debug=False, host="127.0.0.1", port="8050")
