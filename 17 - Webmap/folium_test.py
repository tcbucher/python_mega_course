import folium

# The Map method creates a map object given a location
# location: a list or tuple of lat (-90 to 90) and long (-180 to 180).  values are northing, easting
# zoom_start: an integer specifying the default zoom level.  Higher numbers are more zoomed in
# tiles: the basemap you wish to use, by default this is 'OpenStreetMap'
ftown_coords = (40, -80) # Fredericktown in Western PA
WPAmap = folium.Map(location=ftown_coords, zoom_start=10, tiles='Stamen Terrain') 
# for reference, (38, -98) is a rough geographic center of the continental U.S.

# You can add points to the map using the Marker and CircleMarker methods
# location: a list or tuple of lat (-90 to 90) and long (-180 to 180).  values are northing, easting
# popup: some text to show when the user clicks the point on the map
# icon: an icon to be displayed at the marker.  By default, shows a blue point balloon with a white dot
ftown_icon = folium.Icon(color='green')
ftown_marker = folium.Marker(location=ftown_coords, popup="Fredericktown", icon=ftown_icon)

# A feature group can help you organize your features
feat_group = folium.FeatureGroup(name='Fredericktown')
feat_group.add_child(ftown_marker)

# Use add_child to add the features or feature groups you've created to your map
WPAmap.add_child(feat_group)

# Once you create a map object, you can save it as an html file to be viewed in a browser
WPAmap.save("westernPA.html")
