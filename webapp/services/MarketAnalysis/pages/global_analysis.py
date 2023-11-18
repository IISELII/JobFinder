from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px 
import pandas as pd 


# Import the dataframe 
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    "Date": [2018, 2019, 2020, 2021, 2022, 2023],
})

custom_color_palette = ['#800080',  # Violet
                        '#FFC0CB',  # Rose
                        '#FFA500',  # Orange
                        '#FFFF00']  # Jaune

bar = px.bar(df, x = "Fruit", y = "Amount", color='City', color_discrete_sequence=custom_color_palette, barmode = "group")

bar.update_layout(legend=dict(
    orientation="h", #Horizontale
    yanchor="bottom",
    y=1.05,
    xanchor="center",
    x=0.8),
    margin=dict(t=100)
)

pie = px.pie(df, names = 'Fruit', values = 'Amount', color_discrete_sequence=custom_color_palette, hole = 0.6)

pie.update_layout(legend=dict(
    orientation="h", #Horizontale
    yanchor="bottom",
    y=-0.25,
    xanchor="center",
    x=0.5
))

line = px.line(df, x="Date", y="Amount", color_discrete_sequence=custom_color_palette)

main_page_layout = html.Div(children=[
    
    html.Div([
        
        html.Div([
            html.Div([
                html.P('Weekly Sales'),
                html.H3('$15,000'),
                html.P('Increased by 60%', style={'color': 'green'}),
            ], className='kpi'),

            html.Div([
                html.P('Weekly Orders'),
                html.H3('45,634'),
                html.P('Decreased by 10%', style={'color': 'red'}),
            ], className='kpi'),

            html.Div([
                html.P('Visitors Online'),
                html.H3('95,574'),
                html.P('Increased by 5%', style={'color': 'green'}),
            ], className='kpi'),
        ], className='kpi-row'),
        
        html.Div([
            dcc.Graph(
                id='bar-graph',
                figure=bar
            ),
            
            html.Div([
                dcc.Graph(
                    id='pie-graph',
                    figure=pie
                )
            ], className='donut-chart-container'),    
        ], className='main-content-1'),
        
        dcc.Graph(
            id='line-graph',
            figure=line
        )
    ], className='main-content'),
    
])