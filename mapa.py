import folium
from folium.plugins import FloatImage
import pandas as pd

# Coordenadas iniciales del mapa
boulder_coords = [15.8, -90.5]
mapita = folium.Map(location=boulder_coords, zoom_start=8, control_scale=True)

# Cargar datos de sedes desde el CSV
data_path = "Sedes_Alba_Keneth_Guatemala.csv"  # Asegúrate de que esté en el mismo directorio
sedes = pd.read_csv(data_path, sep=";")

# Agregar departamentos
departamentos = 'deptos_gt.geojson'
style_function2 = lambda x: {'fillColor': '#ffffff', 
                             'color': '#000000', 
                             'fillOpacity': 0.1,
                             'weight': 1,
                             "dashArray": "5, 5"}

folium.GeoJson(
    departamentos, name="Departamentos",
    style_function=style_function2,
    show=True,
    tooltip=folium.features.GeoJsonTooltip(
        fields=['departamen'],  # Use fields from the json file
        aliases=[''],
        style=("background-color: white; color: #000000; font-family: arial; font-size: 12px; padding: 10px;") 
    )
).add_to(mapita)

# Agregar marcadores de sedes con popups estilizados
for _, row in sedes.iterrows():
    popup_html = f"""
    <div style="font-family: Arial; font-size: 12px; padding: 10px; border: 1px solid #ccc; border-radius: 10px; background-color: #f9f9f9;">
        <h4 style="margin: 0; color: #2c3e50;">{row['Departamento']}</h4>
        <p style="margin: 5px 0;">{row['Direccion']}</p>
        <img src="logo.png" alt="Logo Alba-Keneth" style="width: 100px; height: auto; display: block; margin: 0 auto;">
    </div>
    """
    folium.Marker(
        location=[row['Latitud'], row['Longitud']],
        popup=folium.Popup(popup_html, max_width=250),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(mapita)

# Agregar logo en la esquina inferior derecha
logo_path = "logo.png"  # Ruta al logo
float_image = FloatImage(logo_path, bottom=1, right=1, width=5, height=5)
float_image.add_to(mapita)

# Guardar el mapa
mapita.save("index.html")
