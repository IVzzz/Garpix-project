import json
import numpy as np
import fragmentation
import logging
from box import Box
from container import Container

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%I:%M:%S', level=logging.DEBUG)

# Extracting data from json[START]
filename = r"D:\PyProjects\Garpix-project\Data\_vg_85_bgg5jsons\0\30_cl.json"

with open(filename, encoding="utf8") as file:
    base = file.read()

jsonString = '{"a":54, "b": 28}'

aDict = json.loads(base)

container = Container(aDict['cargo_space']['id'], aDict['cargo_space']['size'][0], aDict['cargo_space']['size'][1],
                      aDict['cargo_space']['size'][2],  aDict['cargo_space']['carrying_capacity'])
logging.info(f'Container: id {container.id}, w:{container.width}, h:{container.height}, l{container.length}, cc:{container.maxWeight}')


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
        return qsort(highArray) + equalArray + qsort(lowArray)


boxes = qsort(boxes)
for item in boxes:
    logging.info(item.getBoxData())

# Loading container in x digit(by length)
