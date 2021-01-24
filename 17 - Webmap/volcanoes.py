import folium
import pandas

volc_data = pandas.read_csv('Volcanoes.txt')

lat = list(volc_data['LAT']) 
lon = list(volc_data['LON'])
names = list(volc_data['NAME'])

feat_group = folium.FeatureGroup(name='volcanoes')      
for x, y, name in zip(lat, lon, names):
    feat_group.add_child(folium.Marker(location=(x,y), popup=name))

map_us = folium.Map(location=(38,-96), zoom_start=5)
map_us.add_child(feat_group)
map_us.save('volcano map.html')