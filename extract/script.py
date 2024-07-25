import sys
import json
from os import path

src = sys.argv[1]
out = sys.argv[2]

srcData = {}
with open(path.join(src, "request.json")) as f:
    srcData = json.loads(f.read())

with open(path.join(out, "output.json"), "w+") as f:
    perimeter = srcData.get('perimeter') or ""
    f.write(perimeter)