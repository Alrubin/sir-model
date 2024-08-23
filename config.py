from dataclasses import dataclass


@dataclass
class AppConfig:
    debug: bool = False
    host: str = "127.0.0.1"
    port: str = "8050"


@dataclass
class GraphLayoutSettings:
    overwrite = True
    background_color = "#f8f9fa"
    height = 350
    title = "Popolazione"
    font_size = 18

    margin_bottom = 0
    margin_left = 20
    margin_right = 20
    margin_top = 0

    title_y = 0.98
    title_x = 0.08
    title_xanchor = "left"
    title_yanchor = "top"

    legend_orientation = "h"
    legend_yanchor = "bottom"
    legend_xanchor = "right"
    legend_xaxis = 1
    legend_yaxis = 1.02
