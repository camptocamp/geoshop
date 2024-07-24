import sys
import json

src = sys.argv[1]
out = sys.argv[2]

srcData = {}
with open(src + "/request.json") as f:
    srcData = json.loads(f.read())

with open(out + "/output.json", "w+") as f:
    perimeter = srcData.get('perimeter') or ""
    f.write(perimeter)