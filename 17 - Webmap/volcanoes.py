import folium
import pandas

volc_data = pandas.read_csv('Volcanoes.txt')

lat = list(volc_data['LAT'])
lon = list(volc_data['LON'])
names = list(volc_data['NAME'])
elevations = list(volc_data['ELEV'])

feat_group = folium.FeatureGroup(name='volcanoes')

def get_marker_color(elev):
    if elev <= 1000:
        marker_color = '#00FF00'
    elif elev <= 3000:
        marker_color = '#FFAA00'
    else:
        marker_color = '#FF0000'
    return marker_color

for x, y, name, el in zip(lat, lon, names, elevations):
    msg = f'{name}\n{el}'

    feat_group.add_child(folium.CircleMarker(location=(x,y), popup=msg, radius=7, fill=True, color='#777777', fill_color=get_marker_color(el), opacity=0.6, fill_opacity=0.6))

map_us = folium.Map(location=(38,-96), zoom_start=5)
map_us.add_child(feat_group)
map_us.save('volcano map.html')