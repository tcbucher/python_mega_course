import folium
import pandas

volc_data = pandas.read_csv('Volcanoes.txt')

lat = list(volc_data['LAT'])
lon = list(volc_data['LON'])
names = list(volc_data['NAME'])
elevations = list(volc_data['ELEV'])

feat_group = folium.FeatureGroup(name='volcanoes')
for x, y, name, el in zip(lat, lon, names, elevations):
    msg = name + '\n' + str(el) # TODO: fstring
    feat_group.add_child(folium.Marker(location=(x,y), popup=msg))

map_us = folium.Map(location=(38,-96), zoom_start=5)
map_us.add_child(feat_group)
map_us.save('volcano map.html')