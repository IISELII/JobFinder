import dash
from dash import Input, Output, State, html, dcc, dash_table, MATCH, ALL, ctx
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import pandas as pd
import plotly.graph_objects as go

app = dash.Dash(__name__, suppress_callback_exceptions = True,
    title = 'Plotly Job Market Analysis',
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

server = app.server


def create_main_nav_link(icon, label, href):
    return dcc.Link(
        dmc.Group(
            display='flex',
            style={'flex-direction': 'column', 'margin-bottom':5},
            position='center',
            spacing=10,
            children=[
                dmc.ThemeIcon(
                    DashIconify(icon=icon, width=18),
                    size=25,
                    radius='5',
                    color='indigo',
                    variant='filled',
                    style={'margin-left':10}
                ),
                dmc.Text(label, size='sm', color='gray', style={'font-family':'IntegralCF-Regular'}),
            ]
        ),
        href=href,
        style={'textDecoration': 'none'},
    )

app.layout = html.Div([dmc.Navbar(
    fixed=True,
    width={"base":300},
    p='sm',
    pr='xs',
    pt=0,
    hidden=True,
    hiddenBreakpoint='sm',
    children=[
        dmc.ScrollArea(
            offsetScrollbars=True,
            type='scropll',
            children=[
                dmc.Group(
                    display='flex',
                    style={'flex-direction': 'column'},
                    align='center',
                    position='center',
                    spacing='xs',
                    children=[
                        dmc.Text('Build By: Selmane Kenzari', style={'font-family':'IntegralCF-RegularOblique'}, size='sm'),
                        dmc.Text('Lyon, France', style={'font-family':'IntegrazlCF-RegularOblique'}, size='sm')
                    ]
                ),

                dmc.Divider(label='Barre de navigation', style={'marginBottom': 20, 'marginTop': 5}),
                dmc.Group(
                    display='flex',
                    style={'flex-direction': 'column'},
                    children=[
                        create_main_nav_link(
                            icon='mdi:people-group',
                            label='Vue Global',
                            href=app.get_relative_path("/vue_global"),
                        ),
                        create_main_nav_link(
                            icon='mdi:magnify',
                            label='Rechercher',
                            href=app.get_relative_path("/rechercher"),
                        ),
                        create_main_nav_link(
                            icon='ooui:text-summary-ltr',
                            label='Predictions',
                            href=app.get_relative_path("/summary"),
                        ),
                    ],
                ),
            ],
        ),
    ],
),
])

if __name__ == '__main__':
    app.run_server(debug=True)
