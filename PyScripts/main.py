import json
import fragmentation
import logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%I:%M:%S', level=logging.DEBUG)

# Extracting data from json[START]
filename = r"D:\PyProjects\Garpix-project\Data\_vg_85_bgg5jsons\0\30_cl.json"

with open(filename, encoding="utf8") as file:
    base = file.read()

jsonString = '{"a":54, "b": 28}'

aDict = json.loads(base)

boxes = [("id", "mass", "size", "count", "group_id")]

for box in aDict["cargo_groups"]:
    boxes.append((box["id"], box["mass"], box["size"], box["count"], box["group_id"]))
# Extracting data from json[END]

# Classifying data
classes = {}
classes = fragmentation.fragmentationBoxes(boxes)

logging.info(f"Classified data from {filename}: {classes}")
