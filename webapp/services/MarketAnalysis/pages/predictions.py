from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px 
import pandas as pd 

predictions_page_layout = html.Div(children=[
    html.Div([
        html.H2('Predictions page'),
    ])
])
