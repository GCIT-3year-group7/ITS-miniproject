import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("run_results.csv")
df['metascore'] = df['metascore'].fillna(0)
df.dropna(axis=0, how='any', inplace=True)
df['votes'] = df['votes'].str.replace(',','')
df.votes = df.votes.astype('int')
url_genre = df.genre[0]
genres = url_genre.split(",")[0:]
newgenres = [genre.replace(",","") for genre in genres]
genres = "|".join(newgenres)
def get_genre(url):
        genres = url.split(",")[0:]
        newgenre = [genre.replace("|","") for genre in genres]
        genres = "|".join(newgenre)
        return genres


df['Genres'] = df.genre.map(get_genre)
genre_set=set()
for genre in df.Genres:
    list_genre = genre.split("|")
    genre_set.update(list_genre)
for genre in genre_set:
    df[genre] = [genre in row.split("|") for row in df.Genres]
genredf = df[list(genre_set)]
df.sort_values(by = 'rating', ascending=False)
df.drop(['Action', 'Music', 'Sport', 'Comedy', 'War', 'Horror', 'History', 'Thriller',
         'Crime', 'Adventure', 'Animation', 'Biography', 'Fantasy','Western','Drama','Mystery',
         'Romance','Musical','Sci-Fi', 'Family'], axis = 1, inplace=True)
genredf1 = df.groupby('Genres', sort=False)
genredf1.get_group('Action')
genredf2 = genredf1.get_group('Action')
a = genredf2.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf3 = genredf1.get_group('Music')
b =genredf3.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf4 = genredf1.get_group('War')
c = genredf4.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf5 = genredf1.get_group('Horror')
d = genredf5.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf6 = genredf1.get_group('History')
e = genredf6.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf7 = genredf1.get_group('Crime')
f = genredf7.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf8 = genredf1.get_group('Adventure')
g = genredf8.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf9 = genredf1.get_group('Talk-Show')
h = genredf9.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf10 = genredf1.get_group('Musical')
i = genredf10.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf11 = genredf1.get_group('Biography')
j = genredf11.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf12 = genredf1.get_group('Fantasy')
k = genredf12.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf13 = genredf1.get_group('Animation')
l = genredf13.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf14 = genredf1.get_group('Western')
m = genredf14.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf15 = genredf1.get_group('Reality-TV')
n = genredf15.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf16 = genredf1.get_group('Thriller')
o = genredf16.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf17 = genredf1.get_group('Sport')
p = genredf17.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf18 = genredf1.get_group('Family')
q = genredf18.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf19 = genredf1.get_group('Mystery')
r = genredf19.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf20 = genredf1.get_group('Drama')
s = genredf20.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf21 = genredf1.get_group('Romance')
t = genredf21.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf22 = genredf1.get_group('Sci-Fi')
u = genredf22.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
genredf23 = genredf1.get_group('Comedy')
v = genredf23.nlargest(3, ['rating'])[['title','runtime','genre','rating','votes','metascore']]

a.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Action)')
b.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Music)')
c.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = War)')
d.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Horror)')
e.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = History)')
f.plot.bar(x='title', y='rating', ylabel='Rating',xlabel='Movie Title (Genre = Crime)')
g.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Adventure)')
h.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Talk-Show)')
i.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Musical)')
j.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Biography)')
k.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Fantasy)')
l.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Animation)')
m.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Western)')
n.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Reality-TV)')
o.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Thriller)')
p.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Sport)')
q.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Family)')
r.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Mystery)')
s.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Drama)')
t.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Romance)')
u.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Science Fiction)')
v.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title (Genre = Comedy)')

a1 = genredf2.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a2 = genredf3.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a3 = genredf3.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a4 = genredf4.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a5 = genredf5.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a6 = genredf6.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a7 = genredf7.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a8 = genredf8.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a9 = genredf9.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a10 = genredf10.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a11 = genredf11.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a12 = genredf12.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a13 = genredf13.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a14 = genredf14.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a15 = genredf15.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a16 = genredf16.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a17 = genredf17.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a18 = genredf18.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a19 = genredf19.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a20 = genredf20.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a21 = genredf21.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
a22 = genredf22.nlargest(1, ['rating'])[['title','runtime','genre','rating','votes','metascore']]
framesGraph = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22]
result1 = pd.concat(framesGraph)
genreGraph = ['Action','Music','War','Horror','History','Crime',
              'Adventure','Talk-Show','Musical','Biography','Fantasy',
              'Animation','Western','Reality-TV','Thriller','Sport',
              'Family','Mystery','Drama','Romance','Sci-Fi','Comedy']
result1.plot.bar(x='title', y='rating', ylabel='Rating', xlabel='Movie Title', title='Hightest Movie Rating of each Genre', color='#00ba37', figsize=(15,8))
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import plotly.express as px

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

tabs_styles = {
    'height': '44px',
    'align-items': 'center'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'border-radius': '15px',
    'background-color': '#F2F2F2',
    'box-shadow': '4px 4px 4px 4px lightgrey',

}
tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px',
    'border-radius': '15px',
}

app.layout = html.Div((

    html.Div([
        html.Div([
            html.Div([
                html.H3('Movie Rating Analysis', style = {'margin-bottom': '0px', 'color': 'black', 'textAlign': 'center'}),
            ])
        ], className = "create_container1 four columns", id = "title"),

    ], id = "header", className = "row flex-display", style = {"margin-bottom": "25px"}),

html.Div([
    html.Div([
        dcc.Tabs(id = "tabs-styled-with-inline", value = 'tab-1', children = [
            dcc.Tab(label = 'Tab 1', value = 'tab-1', style = tab_style, selected_style = tab_selected_style),
            dcc.Tab(label = 'Tab 2', value = 'tab-2', style = tab_style, selected_style = tab_selected_style),
        ], style = tabs_styles),
        html.Div(id = 'tabs-content-inline')
    ], className = "create_container3 eight columns", ),
    ], className = "row flex-display"),

    html.Div([
        html.Div([

            html.P('Select Channel', className = 'fix_label', style = {'color': 'black', 'margin-top': '2px', 'display': 'None'}),
            dcc.Dropdown(id = 'select_channels',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'display': 'None'},
                         value = 'Action',
                         placeholder = 'Select Genre',
                         options = [{'label': 'Action', 'value': 'Action'},
                                   {'label': 'Music', 'value': 'Music'},
                                   {'label': 'War', 'value': 'War'},
                                   {'label': 'Horror', 'value': 'Horror'},
                                   {'label': 'History', 'value': 'History'},
                                   {'label': 'Crime', 'value': 'Crime'},
                                   {'label': 'Adventure', 'value': 'Adventure'},
                                   {'label': 'Talk-Show', 'value': 'Talk-Show'},
                                   {'label': 'Musical', 'value': 'Musical'},
                                   {'label': 'Biography', 'value': 'Biography'},
                                   {'label': 'Fantasy', 'value': 'Fantasy'},
                                   {'label': 'Animation', 'value': 'Animation'},
                                   {'label': 'Western', 'value': 'Western'},
                                   {'label': 'Reality-TV', 'value': 'Reality-TV'},
                                   {'label': 'Thriller', 'value': 'Thriller'},
                                   {'label': 'Sport', 'value': 'Sport'},
                                   {'label': 'Family', 'value': 'Family'},
                                   {'label': 'Mystery', 'value': 'Mystery'},
                                   {'label': 'Drama', 'value': 'Drama'},
                                   {'label': 'Romance', 'value': 'Romance'},
                                   {'label': 'Sci-Fi', 'value': 'Sci-Fi'},
                                   {'label': 'Comedy', 'value': 'Comedy'}],
                         className = 'dcc_compon'),

        ], className = "create_container3 four columns", style = {'margin-bottom': '20px'}),
    ], className = "row flex-display"),

        html.Div([
          html.Div([

            dcc.Graph(id = 'top3_chart',
                      style = {'display': 'None'},
                      config = {'displayModeBar': 'hover'}),
        ], className = "create_container3 six columns"),
    ], className = "row flex-display"),

), id= "mainContainer", style={"display": "flex", "flex-direction": "column"})

@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.Div([
                html.Div([
                    html.P('Select Genre', className = 'fix_label', style = {'color': 'black', 'margin-top': '2px'}),
                    dcc.Dropdown(id = 'select_channels',
                                 multi = False,
                                 clearable = True,
                                 disabled = False,
                                 style = {'display': True},
                                 value = 'Action',
                                 placeholder = 'Select Genre',
                                 options = [{'label': 'Action', 'value': 'Action'},
                                   {'label': 'Music', 'value': 'Music'},
                                   {'label': 'War', 'value': 'War'},
                                   {'label': 'Horror', 'value': 'Horror'},
                                   {'label': 'History', 'value': 'History'},
                                   {'label': 'Crime', 'value': 'Crime'},
                                   {'label': 'Adventure', 'value': 'Adventure'},
                                   {'label': 'Talk-Show', 'value': 'Talk-Show'},
                                   {'label': 'Musical', 'value': 'Musical'},
                                   {'label': 'Biography', 'value': 'Biography'},
                                   {'label': 'Fantasy', 'value': 'Fantasy'},
                                   {'label': 'Animation', 'value': 'Animation'},
                                   {'label': 'Western', 'value': 'Western'},
                                   {'label': 'Reality-TV', 'value': 'Reality-TV'},
                                   {'label': 'Thriller', 'value': 'Thriller'},
                                   {'label': 'Sport', 'value': 'Sport'},
                                   {'label': 'Family', 'value': 'Family'},
                                   {'label': 'Mystery', 'value': 'Mystery'},
                                   {'label': 'Drama', 'value': 'Drama'},
                                   {'label': 'Romance', 'value': 'Romance'},
                                   {'label': 'Sci-Fi', 'value': 'Sci-Fi'},
                                   {'label': 'Comedy', 'value': 'Comedy'}], 
                                 className = 'dcc_compon'),

                ], className = "create_container2 six columns", style = {'margin-top': '20px'}),
            ], className = "row flex-display"),
            
            html.Div([
                html.Div([
                    dcc.Graph(id = 'top3_chart',
                              config = {'displayModeBar': 'hover'}),
                ], className = "create_container2 twenty columns", style = {'margin-top': '10px'}),
            ], className = "row flex-display"),
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.Div([
                html.Div([
                    html.P('Select Chart Type', className = 'fix_label', style = {'color': 'black'}),
                    dcc.RadioItems(id = 'radio_items',
                                   labelStyle = {"display": "inline-block"},
                                   options = [
                                       {'label': ' chart', 'value': 'line'},
                                       {'label': 'Donut chart', 'value': 'donut'},
                                       {'label': 'Horizontal bar chart', 'value': 'horizontal'}],
                                   value = 'line',
                                   style = {'text-align': 'center', 'color': 'black'}, className = 'dcc_compon'),

                ], className = "create_container2 six columns", style = {'margin-top': '20px'}),
            ], className = "row flex-display"),

            html.Div([
                html.Div([
                    dcc.Graph(id = 'multi_chart1',
                              config = {'displayModeBar': 'hover'}),

                ], className = "create_container2 ten columns", style = {'margin-top': '10px'}),

            ], className = "row flex-display"),
        ])
    

@app.callback(
Output('top3_chart', 'figure'), 
[Input('select_channels', 'value')]
)
#graph plot and styling
def update_graph(channel):
    if channel == 'Action':
        return {'data':[go.Bar(
                                x = a.rating,
                                y = a.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + a['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + a['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + a['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + a['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Music':
        return {'data':[go.Bar(
                                x = b.rating,
                                y = b.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + b['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + b['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + b['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + b['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'War':
        return {'data':[go.Bar(
                                x = c.rating,
                                y = c.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + c['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + c['rating'].astype(str) + '<br>' + 
                                    '<b>Runtime</b>: ' + c['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + c['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Horror':
        return {'data':[go.Bar(
                                x = d.rating,
                                y = d.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + d['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + d['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + d['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + d['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'History':
        return {'data':[go.Bar(
                                x = e.rating,
                                y = e.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + e['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + e['radius'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + e['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + e['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Crime':
        return {'data':[go.Bar(
                                x = f.rating,
                                y = f.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + f['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + f['rating'].astype(str) + '<br>' + 
                                    '<b>Runtime</b>: ' + f['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + f['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Adventure':
        return {'data':[go.Bar(
                                x = g.rating,
                                y = g.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + g['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + g['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + g['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + g['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }

    if channel == 'Talk-Show':
        return {'data':[go.Bar(
                                x = h.rating,
                                y = h.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + h['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + h['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + h['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + h['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Musical':
        return {'data':[go.Bar(
                                x = i.rating,
                                y = i.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + i['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + i['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + i['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + i['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Biography':
        return {'data':[go.Bar(
                                x = j.rating,
                                y = j.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + j['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + j['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + j['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + j['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Fantasy':
        return {'data':[go.Bar(
                                x = k.rating,
                                y = k.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + k['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + k['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + k['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + k['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Animation':
        return {'data':[go.Bar(
                                x = l.rating,
                                y = l.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + l['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + l['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + l['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + l['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Western':
        return {'data':[go.Bar(
                                x = m.rating,
                                y = m.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + m['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + m['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + m['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + m['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Reality-TV':
        return {'data':[go.Bar(
                                x = n.rating,
                                y = n.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + n['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + n['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + n['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + n['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Thriller':
        return {'data':[go.Bar(
                                x = o.rating,
                                y = o.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + o['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + o['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + o['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + o['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Sport':
        return {'data':[go.Bar(
                                x = p.rating,
                                y = p.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + p['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + p['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + p['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + p['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Family':
        return {'data':[go.Bar(
                                x = q.rating,
                                y = q.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + q['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + q['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + q['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + q['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Mystery':
        return {'data':[go.Bar(
                                x = r.rating,
                                y = r.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + r['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + r['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + r['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + r['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Drama':
        return {'data':[go.Bar(
                                x = s.rating,
                                y = s.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + s['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + s['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + s['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + s['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Romance':
        return {'data':[go.Bar(
                                x = t.rating,
                                y = t.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + t['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + t['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + t['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + t['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Sci-Fi':
        return {'data':[go.Bar(
                                x = u.rating,
                                y = u.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + u['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + u['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + u['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + u['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Comedy':
        return {'data':[go.Bar(
                                x = v.rating,
                                y = v.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + v['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + v['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + v['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + v['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }

@app.callback(Output('multi_chart1', 'figure'),
              [Input('radio_items', 'value')])
def update_graph(radio_items):
    if radio_items == 'line':
        fig = px.bar(
        x = result1.rating, 
        y = result1.title,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark',
        orientation = 'h'
    )
        return fig               

if __name__ == '__main__':
    app.run_server(port=8051)


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import plotly.express as px

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

tabs_styles = {
    'height': '44px',
    'align-items': 'center'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'border-radius': '15px',
    'background-color': '#F2F2F2',
    'box-shadow': '4px 4px 4px 4px lightgrey',

}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px',
    'border-radius': '15px',
}

app.layout = html.Div((

    html.Div([
        html.Div([
            html.Div([
                html.H3('Movie Rating Analysis', style = {'margin-bottom': '0px', 'color': 'black'}),
            ])
        ], className = "create_container1 four columns", id = "title"),

    ], id = "header", className = "row flex-display", style = {"margin-bottom": "25px"}),

html.Div([
    html.Div([
        dcc.Tabs(id = "tabs-styled-with-inline", value = 'tab-1', children = [
            dcc.Tab(label = 'Tab 1', value = 'tab-1', style = tab_style, selected_style = tab_selected_style),
            dcc.Tab(label = 'Tab 2', value = 'tab-2', style = tab_style, selected_style = tab_selected_style),
        ], style = tabs_styles),
        html.Div(id = 'tabs-content-inline')
    ], className = "create_container3 eight columns", ),
    ], className = "row flex-display"),

    html.Div([
        html.Div([

            html.P('Select Genre', className = 'fix_label', style = {'color': 'black', 'margin-top': '2px', 'display': 'None'}),
            dcc.Dropdown(id = 'select_channels',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'display': 'None'},
                         value = 'Action',
                         placeholder = 'Select Genre',
                         options = [{'label': 'Action', 'value': 'Action'},
                                   {'label': 'Music', 'value': 'Music'},
                                   {'label': 'War', 'value': 'War'},
                                   {'label': 'Horror', 'value': 'Horror'},
                                   {'label': 'History', 'value': 'History'},
                                   {'label': 'Crime', 'value': 'Crime'},
                                   {'label': 'Adventure', 'value': 'Adventure'},
                                   {'label': 'Talk-Show', 'value': 'Talk-Show'},
                                   {'label': 'Musical', 'value': 'Musical'},
                                   {'label': 'Biography', 'value': 'Biography'},
                                   {'label': 'Fantasy', 'value': 'Fantasy'},
                                   {'label': 'Animation', 'value': 'Animation'},
                                   {'label': 'Western', 'value': 'Western'},
                                   {'label': 'Reality-TV', 'value': 'Reality-TV'},
                                   {'label': 'Thriller', 'value': 'Thriller'},
                                   {'label': 'Sport', 'value': 'Sport'},
                                   {'label': 'Family', 'value': 'Family'},
                                   {'label': 'Mystery', 'value': 'Mystery'},
                                   {'label': 'Drama', 'value': 'Drama'},
                                   {'label': 'Romance', 'value': 'Romance'},
                                   {'label': 'Sci-Fi', 'value': 'Sci-Fi'},
                                   {'label': 'Comedy', 'value': 'Comedy'}],
                         className = 'dcc_compon'),

        ], className = "create_container3 four columns", style = {'margin-bottom': '20px'}),
    ], className = "row flex-display"),

        html.Div([
          html.Div([

            dcc.Graph(id = 'top3_chart',
                      style = {'display': 'None'},
                      config = {'displayModeBar': 'hover'}),
        ], className = "create_container3 six columns"),
    ], className = "row flex-display"),

), id= "mainContainer", style={"display": "flex", "flex-direction": "column"})

@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.Div([
                html.Div([
                    html.P('Select Genre', className = 'fix_label', style = {'color': 'black', 'margin-top': '2px'}),
                    dcc.Dropdown(id = 'select_channels',
                                 multi = False,
                                 clearable = True,
                                 disabled = False,
                                 style = {'display': True},
                                 value = 'Action',
                                 placeholder = 'Select Channel',
                                 options = [{'label': 'Action', 'value': 'Action'},
                                   {'label': 'Music', 'value': 'Music'},
                                   {'label': 'War', 'value': 'War'},
                                   {'label': 'Horror', 'value': 'Horror'},
                                   {'label': 'History', 'value': 'History'},
                                   {'label': 'Crime', 'value': 'Crime'},
                                   {'label': 'Adventure', 'value': 'Adventure'},
                                   {'label': 'Talk-Show', 'value': 'Talk-Show'},
                                   {'label': 'Musical', 'value': 'Musical'},
                                   {'label': 'Biography', 'value': 'Biography'},
                                   {'label': 'Fantasy', 'value': 'Fantasy'},
                                   {'label': 'Animation', 'value': 'Animation'},
                                   {'label': 'Western', 'value': 'Western'},
                                   {'label': 'Reality-TV', 'value': 'Reality-TV'},
                                   {'label': 'Thriller', 'value': 'Thriller'},
                                   {'label': 'Sport', 'value': 'Sport'},
                                   {'label': 'Family', 'value': 'Family'},
                                   {'label': 'Mystery', 'value': 'Mystery'},
                                   {'label': 'Drama', 'value': 'Drama'},
                                   {'label': 'Romance', 'value': 'Romance'},
                                   {'label': 'Sci-Fi', 'value': 'Sci-Fi'},
                                   {'label': 'Comedy', 'value': 'Comedy'}], 
                                 className = 'dcc_compon'),

                ], className = "create_container2 six columns", style = {'margin-top': '20px'}),
            ], className = "row flex-display"),
            
            html.Div([
                html.Div([
                    dcc.Graph(id = 'top3_chart',
                              config = {'displayModeBar': 'hover'}),
                ], className = "create_container2 twenty columns", style = {'margin-top': '10px'}),
            ], className = "row flex-display"),
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.Div([
                html.Div([
                    html.P('Select Chart Type', className = 'fix_label', style = {'color': 'black'}),
                    dcc.RadioItems(id = 'radio_items',
                                   labelStyle = {"display": "inline-block"},
                                   options = [
                                       {'label': ' chart', 'value': 'line'},
                                       {'label': 'Donut chart', 'value': 'donut'},
                                       {'label': 'Horizontal bar chart', 'value': 'horizontal'}],
                                   value = 'line',
                                   style = {'text-align': 'center', 'color': 'black'}, className = 'dcc_compon'),

                ], className = "create_container2 six columns", style = {'margin-top': '20px'}),
            ], className = "row flex-display"),

            html.Div([
                html.Div([


                    dcc.Graph(id = 'multi_chart1',
                              config = {'displayModeBar': 'hover'}),

                ], className = "create_container2 ten columns", style = {'margin-top': '10px'}),

            ], className = "row flex-display"),
        ])
    

@app.callback(
Output('top3_chart', 'figure'), 
[Input('select_channels', 'value')]
)
#graph plot and styling
def update_graph(channel):
    if channel == 'Action':
        return {'data':[go.Bar(
                                x = a.rating,
                                y = a.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + a['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + a['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + a['runtime'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + a['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + a['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Music':
        return {'data':[go.Bar(
                                x = b.rating,
                                y = b.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + b['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + b['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + b['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + b['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'War':
        return {'data':[go.Bar(
                                x = c.rating,
                                y = c.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + c['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + c['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + c['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + c['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Horror':
        return {'data':[go.Bar(
                                x = d.rating,
                                y = d.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + d['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + d['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + d['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + d['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'History':
        return {'data':[go.Bar(
                                x = e.rating,
                                y = e.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + e['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + e['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + e['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + e['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Crime':
        return {'data':[go.Bar(
                                x = f.rating,
                                y = f.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + f['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + f['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + f['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + f['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Adventure':
        return {'data':[go.Bar(
                                x = g.rating,
                                y = g.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + g['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + g['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + g['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + g['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Talk-Show':
        return {'data':[go.Bar(
                                x = h.rating,
                                y = h.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + h['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + h['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + h['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + h['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Musical':
        return {'data':[go.Bar(
                                x = i.rating,
                                y = i.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + i['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + i['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + i['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + i['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Biography':
        return {'data':[go.Bar(
                                x = j.rating,
                                y = j.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + j['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + j['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + j['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + j['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Fantasy':
        return {'data':[go.Bar(
                                x = k.rating,
                                y = k.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + k['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + k['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + k['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + k['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Animation':
        return {'data':[go.Bar(
                                x = l.rating,
                                y = l.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + l['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + l['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + l['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + l['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Western':
        return {'data':[go.Bar(
                                x = m.rating,
                                y = m.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + m['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + m['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + m['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + m['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Reality-TV':
        return {'data':[go.Bar(
                                x = n.rating,
                                y = n.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + n['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + n['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + n['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + n['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Thriller':
        return {'data':[go.Bar(
                                x = o.rating,
                                y = o.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + o['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + o['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + o['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + o['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Sport':
        return {'data':[go.Bar(
                                x = p.rating,
                                y = p.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + p['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + p['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + p['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + p['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Family':
        return {'data':[go.Bar(
                                x = q.rating,
                                y = q.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + q['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + q['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + q['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + q['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Mystery':
        return {'data':[go.Bar(
                                x = r.rating,
                                y = r.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + r['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + r['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + r['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + r['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Drama':
        return {'data':[go.Bar(
                                x = s.rating,
                                y = s.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + s['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + s['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + s['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + s['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Romance':
        return {'data':[go.Bar(
                                x = t.rating,
                                y = t.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + t['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + t['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + t['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + t['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    
    if channel == 'Sci-Fi':
        return {'data':[go.Bar(
                                x = u.rating,
                                y = u.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + u['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + u['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + u['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + u['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }
    if channel == 'Comedy':
        return {'data':[go.Bar(
                                x = v.rating,
                                y = v.title,
                                orientation = 'h',
                                hoverinfo = 'text',
                                hovertext =
                                    '<b>Name</b>: ' + v['title'].astype(str) + '<br>' +
                                    '<b>Rating</b>: ' + v['rating'].astype(str) + '<br>' +
                                    '<b>Runtime</b>: ' + v['runtime'].astype(str) + '<br>' + 
                                    '<b>Votes</b>: ' + v['votes'].astype(str) + '<br>'
                                ),
                             ] ,
                'layout': go.Layout(
                            plot_bgcolor = '#F2F2F2',
                            paper_bgcolor = '#F2F2F2',
                            title = {
                                    'text': 'Top 3 Movie of :' + ' ' + (channel),
                                    'y': 0.9,
                                    'x': 0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            titlefont = {
                                     'color': 'black',
                                     'size': 18},
                            hovermode = 'closest',
                            margin = dict(l = 300),
                        
                            xaxis=dict(
                                #type='line',
                                title='<b>Rating</b>',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),
                            yaxis=dict(
                                title= '<b>Movie Title Name</b>',
                                autorange = 'reversed',
                                color = 'black',
                                showgrid=True,
                                showline=True,
                                showticklabels = True,
                                linecolor = 'black',
                                linewidth = 1,
                                ticks = 'outside',
                                tickfont = dict(
                                    family = 'Arial',
                                    size = 11,
                                    color = 'black'
                                )
                            ),                         
                        )    
               }

@app.callback(Output('multi_chart1', 'figure'),
              [Input('radio_items', 'value')])
def update_graph(radio_items):
    if radio_items == 'line':
        fig = px.bar(
        x = result1.rating, 
        y = result1.title,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark',
        orientation = 'h'
    )
        return fig 

if __name__ == '__main__':
    app.run_server(port=8051)