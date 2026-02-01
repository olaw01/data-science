import dash
from dash import dcc, html
import plotly.graph_objects as go


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H2(children = 'Hello Dash!'),

    dcc.Graph(
        figure  = go.Figure([
            go.Bar(
                x=['2017', '2018', '2019', '2020'],
                y=[1, 2, 3, 4],
                name = 'Lokalnie'
            ),
        go.Bar(
            x=['2017', '2018', '2019', '2020'],
            y=[13, 232, 33, 411],
            name='online'
        )
    ])
    )
])

if __name__ == '__main__':
    app.run(debug=True)