from dash import html, dcc
import dash

dash.register_page(
    __name__,
    name='NYC Street Trees',
    top_nav=True,
    path='/'
)


def layout():

    """
    Generates home page html
    :return: HTML/Dash Object(s)
    """

    layout = html.Div(
        [
            dcc.Markdown(f"""This map shows where the trees have been planted through the 
            [NYC Street Tree Planting initiative](https://www.nycgovparks.org/trees/street-tree-planting). The number 
            of trees planted in each area is indicated by the height and color of the hexagons on the map. For more 
            information please see our [About](/about) page. The toggle in the upper left corner of the map will allow 
            you to explore the data more thoroughly and the settings of the map can be tuned to your preference.""")
        ],
        style={'margin': '5% 5% 5% 5%'}
    )
    return layout
