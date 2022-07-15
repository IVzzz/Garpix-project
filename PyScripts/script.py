import json

import fragmentation

filename = r"_vg_85_bgg5jsons\0\30_cl.json"

with open (filename, encoding="utf8") as file:

	base = file.read()

jsonString = '{"a":54, "b": 28}'

aDict = json.loads (base)

# boxes = [("id", "mass", "size", "sort", "count", "stacking", "turnover", "overhang_angle", "stacking_limit", "stacking_is_limited", "group_id")]

boxes = [("id", "mass", "size", "count", "group_id")]

for box in aDict["cargo_groups"]:

#	boxes.append( (box["id"], box["mass"], box["size"], box["sort"], box["count"], box["stacking"], box["turnover"], box["overhang_angle"], box["stacking_limit"], box["stacking_is_limited"], box["group_id"]) )
	boxes.append( (box["id"], box["mass"], box["size"], box["count"], box["group_id"]) )

#   print (boxes)

classes_ = {}

classes_ = fragmentation.fragmentationBoxes(boxes)

#  print(classes_.keys())
print(classes_)