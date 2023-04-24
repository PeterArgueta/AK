import folium
from folium.plugins import FloatImage

boulder_coords=[15.8,-90.5]

mapita=folium.Map(location=boulder_coords, zoom_start= 8, control_scale=True)



departamentos='deptos_gt.geojson'

style_function2 = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1,
                            'weight':1,
                            "dashArray": "5, 5"}

folium.GeoJson(
    departamentos, name="Departamentos",
    style_function=style_function2,
    show=(True),
     tooltip=folium.features.GeoJsonTooltip(
        fields=['departamen'],  # use fields from the json file
        aliases=[''],
        style=("background-color: white; color: #000000; font-family: arial; font-size: 12px; padding: 10px;") 
    )
).add_to(mapita)




mapita.save("index.html")
