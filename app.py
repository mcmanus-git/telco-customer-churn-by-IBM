import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from navbar import create_navbar
from footer import create_footer

# Toggle the themes at [dbc.themes.LUX]
# The full list of available themes is:
# BOOTSTRAP, CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, PULSE, SANDSTONE,
# SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI, ZEPHYR.
# https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/

navbar = create_navbar()
footer = create_footer()
FA47 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
FA512 = "https://use.fontawesome.com/releases/v5.12.1/css/all.css"

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.FLATLY,
                                      FA47,
                                      FA512,
                                      ],
                use_pages=True,
                )


app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>NYC Street Trees</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        
    </body>
</html>
'''

# app.layout = dcc.Loading(
#     id='loading_page_content',
#     children=[
#         html.Div(
#             [
#                 navbar,
#                 dash.page_container
#             ],
#             style={"width": "100vw", "height": "100vh"}
#         )
#     ],
#     color='#333B52',
#     fullscreen=True
# )

app.layout = dbc.Container(
    [
        navbar,
        dash.page_container,
        footer
    ],
    fluid=True,
    style={
        "padding": "0px",
        "height": "100vh"
    },
)

server = app.server

if __name__ == '__main__':
    app.run_server(debug=False)
