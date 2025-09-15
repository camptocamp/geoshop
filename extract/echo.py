import json
import os
import sys

src = sys.argv[1]
out = sys.argv[2]

data = {}
with open(os.path.join(src, "request.json"), "r") as f:
    data = json.load(f)

with open(os.path.join(out, "response.json"), "w") as f:
    json.dump(data, f)
