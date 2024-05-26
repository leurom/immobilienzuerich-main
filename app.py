from flask import Flask, render_template, request, jsonify
import geopandas as gpd
from shapely.geometry import Point
import os
import math


app = Flask(__name__, template_folder='static')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.is_json:
        data = request.get_json()
        lat = data['lat']
        lng = data['lng']

        # Log received coordinates
        print(f"Received latitude: {lat} and longitude: {lng}")

        # Calculate and fetch nearest neighbor data
        nodes = find_nearest_neighbor(lat, lng)
        number_of_nodes = len(nodes)

        print("Number of nodes within 1 kilometer:", number_of_nodes)
        coefficient = getcoefficient(number_of_nodes)
        # Respond back to the client with results
        response = {
            "status": "success",
            "message": "Coordinates received",
            "amount_nearest_neighbor": number_of_nodes,
            "coefficient": coefficient
        }
        return jsonify(response)
    else:
        return jsonify({"status": "error", "message": "Request was not JSON"}), 400

def find_nearest_neighbor(lat, lng):
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, 'static', 'geodata.gpkg')
    print(f"Filepath: {file_path}")

    # Load GeoDataFrame from a GeoPackage file
    layer_name = 'all'
    print(f"Layer name: {layer_name}")
    gdf = gpd.read_file(file_path, layer=layer_name)

    # Check current CRS
    print(f"Current CRS: {gdf.crs}")

    # Convert CRS to EPSG:2056 for accurate distance calculation
    gdf = gdf.to_crs(epsg=2056)

    # Define the reference location as a Shapely Point and convert CRS
    reference_location = Point(lng, lat)
    # Create a GeoDataFrame for the reference point to convert CRS
    gdf_point = gpd.GeoDataFrame([1], geometry=[reference_location], crs='EPSG:4326')  # WGS84 Latitude and Longitude
    gdf_point = gdf_point.to_crs(epsg=2056)
    reference_location = gdf_point.geometry[0]

    # Calculate distances from the reference location to each geometry in the GeoDataFrame
    gdf['distance'] = gdf.geometry.distance(reference_location)

    # Filter to find nodes within 1 kilometer (1000 meters)
    nodes_within_1km = gdf[gdf['distance'] <= 1000]  # Adjust this value to 50 if needed
    print(nodes_within_1km)
    # Count the nodes within 1 kilometer
    number_of_nodes = len(nodes_within_1km)

    # Get minimum and maximum distances within 1 km
    min_distance = nodes_within_1km['distance'].min()
    max_distance = nodes_within_1km['distance'].max()

    # Normalisierung des Koeffizienten auf einen Bereich von 0 bis 2
    normalized_coefficient = (number_of_nodes - 1) / 1100
    coefficient = normalized_coefficient*2
    # Anwendung einer logarithmischen Funktion, um ein nichtlineares Wachstum zu erzielen
    #coefficient = 2 * math.log10(normalized_coefficient + 1)
    # Respond with the coefficient
    response = {
        "status": "success",
        "message": "Coordinates received",
        "coefficient": coefficient
    }

    print(f"Number of nodes within 1 kilometer: {number_of_nodes}")
    print(jsonify(response))
    return nodes_within_1km

def getcoefficient(number_of_nodes):
    normalized_coefficient = (number_of_nodes - 1) / 1100
    coefficient = normalized_coefficient*2
    return coefficient

if __name__ == '__main__':
    app.run(debug=True)

def find_nearest_neighbor2(lat, lng):
    # SQL-Abfrage für die nächstgelegenen Knoten innerhalb von 1 Kilometer
    sql = """
         SELECT * FROM nodes
         WHERE ST_Distance(ST_Point(:lat, :lng), geometry) <= 1000
     """
    cursor.execute(sql, {"lat": lat, "lng": lng})
    nodes = cursor.fetchall()

