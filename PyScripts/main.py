import json
import numpy as np
import fragmentation
import logging
from box import Box

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%I:%M:%S', level=logging.DEBUG)

# Extracting data from json[START]
filename = r"D:\PyProjects\Garpix-project\Data\_vg_85_bgg5jsons\0\30_cl.json"

with open(filename, encoding="utf8") as file:
    base = file.read()

jsonString = '{"a":54, "b": 28}'

aDict = json.loads(base)

#boxes = [("id", "mass", "size", "count", "group_id")]
boxes = []

for item in aDict["cargo_groups"]:
    boxes.append(Box(item['id'], item['group_id'], item['size'][0], item['size'][1], item['size'][2], item['count'], item['mass']))
# Extracting data from json[END]

# Classifying data
# classes = {}
# classes = fragmentation.fragmentationBoxes(boxes)

logging.info(f"Classified data from {filename}")
