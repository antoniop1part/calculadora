import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

app = Dash(__name__)




app.layout = html.Div([

    html.H1('Creator Kit', id='h1'),
    html.H2('Responda para ganhar 30 dias grátis!'),

    html.Label('Checklist'),
    dcc.Checklist(
    ['New York City', 'Montréal', 'San Francisco'],
    inline=True,
    id='check2', 
),

dcc.Dropdown(
    
    ['New York City', 'Montréal', 'San Francisco'], 'San Francisco',
    id='dp'
),


dcc.Slider(0, 20, 5, value=10, id='sld')

])
    
if __name__ == '__main__':
    app.run_server(debug=True)