import csv
import ast
import folium # interactive maps
from folium.plugins import MarkerCluster

coords = []
addresses = []

with open('address_output_f.csv', mode='r') as f:
    # since coords are in tuple string form, convert them to tuples
    reader = csv.DictReader(f)
    for row in reader:
        coords.append(ast.literal_eval(row['Coordinates']))
        addresses.append(row['Property Location'])

# print(len(coords))
# print(addresses)

# copied from documentation
map = folium.Map(location=coords[0], zoom_start=15) # centering
cluster = MarkerCluster().add_to(map)

for (latitutde, longitude), address in zip(coords, addresses):
    folium.Marker([latitutde, longitude], popup=address).add_to(cluster)

map.save("map.html")
