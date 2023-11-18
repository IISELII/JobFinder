from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px 
import pandas as pd 

detail_analysis_page_layout = html.Div(children=[
    html.Div([
        html.H2('Detail analysis page'),
    ])
])