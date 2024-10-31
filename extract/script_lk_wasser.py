import sys
import psycopg2
import geopandas as gpd
from os import path
import json
from shapely import wkt


src = sys.argv[1]
out = sys.argv[2]

perimeter = None
with open(path.join(src, "request.json")) as f:
    srcData = json.loads(f.read())
    perimeter = srcData.get('perimeter')

if not perimeter:
    print("Error: no perimeter defined")
    sys.exit(-1)

# Connect to the PostgreSQL database
conn = psycopg2.connect(database=os.environ["UGSP_POSTGRES_DB"],
                        host=os.environ["UGSP_POSTGRES_HOST"],
                        user=os.environ["UGSP_POSTGRES_USER"],
                        password=os.environ["UGSP_POSTGRES_PASSWORD"])
cur = conn.cursor()

# Define the output GeoPackage path
output_gpkg = path.join(out, "output.gpkg")

# Function to fetch data from a table and return as GeoDataFrame
def fetch_table_as_gdf(table_name, perimeter=perimeter):
    query = f"SELECT * FROM lk_map_wasser.{table_name}"
    # Check if a perimeter is provided and add spatial filtering to the query
    params = (perimeter,)
    if perimeter:
        try:
            # Ensure the perimeter is in WKT format and parse it with Shapely to validate
            wkt.loads(params)  # This will raise an error if `perimeter` is not valid WKT
            
            # Add spatial filtering to the query using perimeter
            query = f"""
                SELECT *
                FROM lk_map_wasser.{table_name}
                WHERE ST_Intersects(
                    geom,
                    ST_Transform(ST_GeomFromText(%s, 4326), 2056));
                """         
        except Exception as e:
            print("Error: Invalid WKT format for perimeter.")
            return None
    # Load data into a GeoDataFrame
    gdf = gpd.read_postgis(query, conn, geom_col='geom', params=params)
    # Set the CRS (EPSG:2056)
    gdf.set_crs(epsg=2056, inplace=True)
    return gdf

# Fetch each table as a GeoDataFrame if not empty
flaeche_gdf = fetch_table_as_gdf('p_wasser_flaeche')
linie_gdf = fetch_table_as_gdf('p_wasser_linie')
punkt_gdf = fetch_table_as_gdf('p_wasser_punkt')
text_gdf = fetch_table_as_gdf('p_wasser_text')


# Write each GeoDataFrame to a separate layer in the GeoPackage if it is not empty
if flaeche_gdf is not None and not flaeche_gdf.empty:
    flaeche_gdf.to_file(output_gpkg, layer='p_wasser_flaeche', driver='GPKG')

if linie_gdf is not None and not linie_gdf.empty:
    linie_gdf.to_file(output_gpkg, layer='p_wasser_linie', driver='GPKG')

if punkt_gdf is not None and not punkt_gdf.empty:
    punkt_gdf.to_file(output_gpkg, layer='p_wasser_punkt', driver='GPKG')

if text_gdf is not None and not text_gdf.empty:
    text_gdf.to_file(output_gpkg, layer='p_wasser_text', driver='GPKG')


# Close the connection
conn.close()

print(f"GeoPackage created: {output_gpkg}")