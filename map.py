import json
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout

#filename = "/Users/bernardlipat/Documents/coddin"
from pickletools import long1
from syslog import LOG_NEWS


data = {"type" : "scattergeo"}
    'lon' ; lons
    'lat' ; lats
    #'text' ; hover_texts,
    #   'marker'
    #   
}]
my_layout = Layout(title='Global Earthquake')
fig = {'data': data, 'layout' : my_layout}
offline.plot(fig,filename='global_earthquakes.html')
