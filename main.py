
# python main.py
# http://127.0.0.1:5000/

from flask import Flask
import folium

app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (55.5940700, 37.5160300)
    tooltip = "Нажми меня!"
    folium_map = folium.Map(location=start_coords, tiles="Stamen Terrain", zoom_start=9)

    folium.Marker(
        location=[55.6240700, 37.5160300],
        popup="<i>Москва</i>", tooltip=tooltip,
        icon=folium.Icon(color="green")
    ).add_to(folium_map)

    folium.Marker(
        location=[55.6140700, 37.5160300],
        popup="Метка", tooltip=tooltip,
        icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(folium_map)

    folium.Marker(
        location=[55.6040700, 37.5160300],
        popup="Moscow",
        icon=folium.Icon(icon="cloud"),
    ).add_to(folium_map)

    folium.Marker(
        location=[55.5940700, 37.5160300],
        popup="<i>Москва</i>", tooltip=tooltip,
    ).add_to(folium_map)





    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
