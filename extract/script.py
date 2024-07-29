import json
import sys
from osgeo import ogr
from os import path

src = sys.argv[1]
out = sys.argv[2]

srcData = {}
with open(path.join(src, "request.json")) as f:
    srcData = json.loads(f.read())

with open(path.join(out, "output.json"), "w+") as f:
    perimeter = srcData.get('perimeter') or ""
    if perimeter:
        geomcol = ogr.CreateGeometryFromWkt(perimeter)
        f.write("Geometry:\n")
        for geom in range(0, geomcol.GetGeometryCount()):
            f.write("\tPoints:\n")
            for pt in geomcol.GetGeometryRef(geom).GetPoints():
                f.write(f"\t\t{pt}\n")
