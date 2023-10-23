import dash
from dash import Input, Output, State, html, dcc, dash_table, MATCH, ALL, ctx
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

app = dash.Dash(__name__, suppress_callback_exceptions = True,
    title = 'Plotly Job Market Analysis',
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

server = app.server

app.layout = html.Div(
    style={'margin-top':'70px'},
    children=[
        dmc.Group(
            display='flex',
            style={'flex-direction': 'column', 'margin-bottom':5},
            grow=True,
            children=[
                dmc.Title(children='Customer Base', order=3, style={'font-family':'IntegralCF-ExtraBold', 'text-align':'center', 'color':'slategray'}),
                dmc.Divider(label='Overview', labelPosition='center', size='x1'),
                dmc.Group(
                    display='flex',
                    style={'flex-direction': 'row', 'margin-bottom':5},
                    grow=True,
                    children=[
                        dmc.Paper(
                            radius='md',
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'175px'},
                            children=[
                                dmc.Center(
                                    dmc.ThemeIcon(
                                        size=50,
                                        radius='x1',
                                        color='violet',
                                        variant='light',
                                        children=[DashIconify(icon='fluent:people-community-20-filled', width=30)]
                                    )
                                ),
                                dmc.Group(
                                    display='flex',
                                    style={'flex-direction': 'column', 'margin-bottom':5, 'margin-top':10},
                                    position='center',
                                    spacing='xs',
                                    children=[
                                        dmc.Text("Total d'offres d'emploi", size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique'}),
                                        # dmc.Text(id='total_offres_emploi', size='x1', style={'font-family':'IntegralCF-ExtraBold'})
                                    ]
                                )
                            ],
                        ),

                        dmc.Paper(
                            radius='md',
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'175px'},
                            children=[
                                dmc.Center(
                                    dmc.ThemeIcon(
                                        size=50,
                                        radius='x1',
                                        color='violet',
                                        variant='light',
                                        children=[DashIconify(icon='fluent:people-community-20-filled', width=30)]
                                    )
                                ),
                                dmc.Group(
                                    display='flex',
                                    style={'flex-direction': 'column', 'margin-bottom':5, 'margin-top':10},
                                    position='center',
                                    spacing='xs',
                                    children=[
                                        dmc.Text("Total d'offres d'emploi", size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique'}),
                                        # dmc.Text(id='total_offres_emploi', size='x1', style={'font-family':'IntegralCF-ExtraBold'})
                                    ]
                                )
                            ],
                        ),

                        dmc.Paper(
                            radius='md',
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'175px'},
                            children=[
                                dmc.Center(
                                    dmc.ThemeIcon(
                                        size=50,
                                        radius='x1',
                                        color='violet',
                                        variant='light',
                                        children=[DashIconify(icon='fluent:people-community-20-filled', width=30)]
                                    )
                                ),
                                dmc.Group(
                                    display='flex',
                                    style={'flex-direction': 'column', 'margin-bottom':5, 'margin-top':10},
                                    position='center',
                                    spacing='xs',
                                    children=[
                                        dmc.Text("Total d'offres d'emploi", size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique'}),
                                        # dmc.Text(id='total_offres_emploi', size='x1', style={'font-family':'IntegralCF-ExtraBold'})
                                    ]
                                )
                            ],
                        ),
                    ],
                ),

                dmc.Divider(label = 'Demographics', labelPosition='center', size='xl'),
                dmc.Group(
                    display='flex',
                    style={'flex-direction': 'row', 'margin-bottom':5},
                    grow = True,
                    children = [
                        dmc.Paper(
                            radius="md", # or p=10 for border-radius of 10px
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'350px'},
                            children=[
                                dmc.Title('Contrat Type', order = 4, style = {'font-family':'IntegralCF-Regular','text-align':'center', 'color':'grey', 'letter-spacing':'1px'}),
                                # ddk.Graph(id='gender'),
                            ]
                        ),
                        dmc.Paper(
                            radius="md", # or p=10 for border-radius of 10px
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'350px'},
                            children=[
                                dmc.Title('Contrat Type', order = 4, style = {'font-family':'IntegralCF-Regular','text-align':'center', 'color':'grey', 'letter-spacing':'1px'}),
                                # ddk.Graph(id='household')
                            ]
                        ),
                    ]
                ),
                dmc.Group(
                    display='flex',
                    style={'flex-direction': 'row', 'margin-bottom':5},
                    grow = True,
                    children = [
                        dmc.Paper(
                            radius="md", # or p=10 for border-radius of 10px
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height':'500px'},
                            children=[
                                dmc.Title("Total offres d'emploi par mois", order = 4, style = {'font-family':'IntegralCF-Regular','text-align':'center', 'color':'grey', 'letter-spacing':'1px'}),
                                # ddk.Graph(id = 'locations_map')
                            ]
                        ),
                    ]
                ),

                dmc.Space(h=50)
            ]
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
