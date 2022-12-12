import dash_bootstrap_components as dbc
import dash.html as html
from dash import dcc


def create_footer():

    footer = html.Footer(
        [
            "Some Text"
        ]
    )

    return footer