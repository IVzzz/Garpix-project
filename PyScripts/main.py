import json
import numpy as np
import fragmentation
import logging
from box import Box

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%I:%M:%S', level=logging.DEBUG)

# Extracting data from json[START]
filename = r"_vg_85_bgg5jsons\0\30_cl.json"

with open(filename, encoding="utf8") as file:
    base = file.read()

jsonString = '{"a":54, "b": 28}'

aDict = json.loads(base)

boxes = []

for item in aDict["cargo_groups"]:
    boxes.append(Box(item['id'], item['group_id'], item['size'][0], item['size'][1], item['size'][2], item['count'], item['mass']))
# Extracting data from json[END]

# Sorting data by non-growth (quicksort)
def qsort(array):
    if len(array) <= 1:
        return array
    else:
        lowArray = []
        highArray = []
        equalArray = [] 

        pivot = array[int(len(array) / 2)].length
        for item in array:
            if item.length < pivot:
                lowArray.append(item)
            elif item.length > pivot:
                highArray.append(item)
            else:
                equalArray.append(item)
        return qsort(lowArray) + equalArray + qsort(highArray)


for item in boxes:
    logging.info(item.getBoxData())

boxes = qsort(boxes)

for item in boxes:
    logging.info(item.getBoxData())

fragmentBoxes = fragmentation.fragmentationBoxes(boxes)

fragmentBoxes = qsort(fragmentBoxes)

for item in fragmentBoxes:
    logging.info(item.getBoxData())

