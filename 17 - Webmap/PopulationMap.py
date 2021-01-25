import folium
import pandas

MILLION = 10**6

sf = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10*MILLION
else 'orange' if 10*MILLION <= x['properties']['POP2005'] < 100*MILLION
else 'red'}

world_file = open('world.json', 'r', encoding='utf-8-sig').read()
pop_overlay = folium.FeatureGroup(name='Population Map')
pop_overlay.add_child(folium.GeoJson(data=world_file, style_function=sf)) # style_function applies to each of the 'features' in the GeoJson

base_map = folium.Map(location=(0,0), zoom_start=2)
base_map.add_child(pop_overlay)

# Add interactive layer control to the map
# Must go after the other features that you want to control
# It will control each feature added as a child to the map, including entire featuregroups
base_map.add_child(folium.LayerControl()) 

base_map.save('Population Map.HTML')