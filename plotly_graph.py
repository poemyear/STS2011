import plotly

user_name = 'poemyeard'
api_key = 'jsCUOzjzyjF19LT9TAG1'
stream_id = '2l57xi43q2'
plotly.tools.set_credentials_file(username=user_name, api_key=api_key)

import math
import plotly.plotly as py
import plotly.graph_objs as go


stream_1 = dict(token=stream_id, maxpoints=60)

trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_1
)

data = go.Data([trace1])

layout = go.Layout(title='Time Series')
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='python-streaming')

s = py.Stream(stream_id)
s.open()

import datetime
import time
import random

time.sleep(5)

x = 0
while True:

    y = math.sin(math.pi * (x/180)) + math.sin(math.pi * 20 * (x/180))/7
    s.write(dict(x=x, y=y))
    time.sleep(0.1)
    x = x+1

s.close()


