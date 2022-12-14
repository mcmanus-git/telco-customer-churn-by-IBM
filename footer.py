import dash_bootstrap_components as dbc
import dash.html as html
from dash import dcc


def create_footer():

    # footer = html.Footer(
    #     [
    #         html.P(["Some Text"])
    #     ],
    #     style={
    #         "background-color": "#2B3E50",
    #         # "min-height": "5vh",
    #         "padding": "16px",
    #         "color": "white"
    #     }
    # )

    footer = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink([html.I(className="fab fa-github")],
                                    href="https://github.com/mcmanus-git",
                                    target="_blank")
                        ),
            dbc.NavItem(dbc.NavLink([html.I(className="fab fa-medium")],
                                    href="https://medium.com/@mcmanus_data_works",
                                    target="_blank")
                        ),
            dbc.NavItem(dbc.NavLink([html.I(className="fab fa-linkedin")],
                                    href="https://www.linkedin.com/in/michael-mcmanus/",
                                    target="_blank")
                        ),
        ],
        brand="TelCom",
        brand_href="/",
        color="primary",  # Change this to change color of the navbar e.g. "primary", "secondary", "dark" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
        expand=True,
        fluid=True,
    )

    return footer
