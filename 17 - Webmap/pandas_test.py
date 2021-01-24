import folium
import pandas

# Read in a dataframe from a csv
# the first line is treated as the header which describes each data column
volc_data = pandas.read_csv("volcanoes.txt")

volc_data.columns # A list of the columns in the dataframe
volc_data["LAT"] # A series of the data in the specified column
list(volc_data["LON"]) # Converts the LON series into a list

