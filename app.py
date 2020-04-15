import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

df = pd.read_csv('Player_Clusters.csv')

app = dash.Dash()

app.layout = html.Div(children=
        [html.H1('Hockey Player Classifyer'),
         html.H3('Cluster Names: '),
         html.H6("Elite Offensive Players (Don't Take FO)"),
         html.H6('Elite Offensive Players (Take FO)'),
         html.H6('Power-Play Specialists'),
         html.H6('Well-Rounded Elite Playmakers (Take FO)'),
         html.H6('Elite Offensive Defensemen'),
         html.H6('Goal Scorers Who Take Penalties'),
         html.H6('Every Situation Forwards'),
         html.H6('Two-Way, FO-Taking Forwards'),
         html.H6('Every Situation Defensemen'),
         html.H6('Strong Defensive Defensemen'),
         html.H6('Lower-Line Skill Players'),
         html.H6('Goal-Focused Lower-Line Players'),
         html.H6('Even Strength two-way defensemen'),
         html.H6('Volume Shooters'),
         html.H6('Big Hitters And PK (No FO)'),
         html.H6('Big Hitters And PK (Take FO)'),
         html.H6('PK Specialist And Shot-Blocking Defensemen'),
         html.H6('Lower-Line PP Defensemen/Defensemen-Like Forwards'),
         html.H6('Physical Defensive Lower-Line Forwards'),
         html.H6('Even Strength Lower-Line Defensive Players'),
         dcc.Input(id='input', value = 'Player or Cluster Name', type = 'text'),
         html.Div(id='output')
        ],
         style={'verticalAlign':'middle',
                'textAlign': 'center',
                'backgroundColor':'pink',
                'fontColor':'red',
                'width':'100%',
                'height':'100%',
                'top':'0px',
                'left':'0px',
                'z-index':'1000'},
        )

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')])

def update_value(input_data) :
    counter = 0
    for index, row in df.iterrows():
        if row['Player'] == input_data:
            cluster = row['cluster_name']
            player_list = []
            for index, row in df.iterrows():
                if row['cluster_name'] == cluster:
                    player_list.append(row['Player'])
            return "{}: {}".format(cluster, player_list)
        elif row['cluster_name'] == input_data:
            cluster = row['cluster_name']
            player_list = []
            for index, row in df.iterrows():
                if row['cluster_name'] == cluster:
                    player_list.append(row['Player'])
            return "{}: {}".format(input_data, player_list)
    return "Please Enter Valid Player or Cluster Name"

if __name__ == '__main__':
    app.run_server(debug = True, host= '127.0.0.1')
