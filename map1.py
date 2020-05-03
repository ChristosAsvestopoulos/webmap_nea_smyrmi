# web map creation using Python and folium and pandas libraries
import pandas as pd
import folium

data = pd.read_csv("nea_smyrni.csv")
lat = list(data["LAT"])
# print(lat)
lon = list(data["LON"])
# print(lon)
desc = list(data["DESC"])
# print(desc)
name = list(data["NAME"])
# print(name)
type_ = list(data["TYPE"])
# print(type_)
link = list(data["LINK"])
# print(link)


def color_producer(typ):
    if typ == "culture":
        return "green"
    elif typ == "sports":
        return "black"
    else:
        return "red"


html = '<h5>{}:</h5>{}<br><a href="{}" target="_blank">Available Link</a>'

# creation of Map Object
map1 = folium.Map(location=[37.946738, 23.714598],  # Latitude and Longitude of Nea Smyrni Square
                  zoom_start=15,  # starting zoom point
                  tiles="OpenStreetMap")  # alternatively: tiles = "Stamen Terrain"

# creation of FeatureGroup Object
fg = folium.FeatureGroup(name="My Map")

for lt, ln, dsc, nm, tp, lnk in zip(lat, lon, desc, name, type_, link):
    iframe = folium.IFrame(html=html.format(nm, dsc, lnk), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=(lt, ln),
                                     radius=5,
                                     popup=folium.Popup(iframe),
                                     fill_color=color_producer(tp),
                                     color='black',
                                     fill_opacity=0.7))

map1.add_child(fg)
map1.add_child(folium.LayerControl())

map1.save("Map1.html")
