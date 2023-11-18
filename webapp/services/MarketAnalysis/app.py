from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px 
import pandas as pd 

from pages.global_analysis import main_page_layout
from pages.detail_analysis import detail_analysis_page_layout
from pages.predictions import predictions_page_layout

app = Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
            html.H2('Sidebar Content'),
            # Add your sidebar elements here 
            dcc.Dropdown(
                id='dropdown-filter',
                options=[
                    {'label': 'Option 1', 'value': 'option1'},
                    {'label': 'Option 2', 'value': 'option2'}
                ],
                value='option1'
            ),
            html.Hr(),
            html.P([
                dcc.Link('Global Analysis', href='/pages/global_analysis')
            ], className='link'),
            html.P([
                dcc.Link('Detail Analysis', href='/pages/detail_analysis'),
            ], className='link'),
            html.P([
                dcc.Link('Predictions', href='/pages/predictions'),
            ], className='link')
        ], className='sidebar'),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/pages/global_analysis':
        return main_page_layout
    elif pathname == '/pages/detail_analysis':
        return detail_analysis_page_layout  
    elif pathname == '/pages/predictions':
        return predictions_page_layout  
    else:
        return "404 Page Not Found" 

if __name__ == '__main__':
    app.run(debug=True)