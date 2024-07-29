import json
import os
import sys
from osgeo import ogr
from os import path
import psycopg2
import geopandas

src = sys.argv[1]
out = sys.argv[2]

conn = psycopg2.connect(database=os.environ["GEODATA_POSTGRES_DB"],
                        host=os.environ["GEODATA_POSTGRES_HOST"],
                        user=os.environ["GEODATA_POSTGRES_USER"],
                        password=os.environ["GEODATA_POSTGRES_PASSWORD"])
dbdf = geopandas.read_postgis("SELECT * FROM polygons", conn)
conn.close()

requestdf = None
with open(path.join(src, "request.json")) as f:
    srcData = json.loads(f.read())
    perimeter = srcData.get('perimeter')
    if perimeter:
        requestdf = geopandas.GeoSeries.from_wkt([perimeter])

with open(path.join(out, "output.json"), "w+") as f:
    f.write("RESULT\n")
    f.write(f"DB: {dbdf}\n\n")
    f.write(f"REQUEST: {requestdf}\n\n")
    if dbdf is not None and requestdf is not None:
        f.write(f"TOUCH_CHECK: \n")

