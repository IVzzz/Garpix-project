import json
import numpy as np
import fragmentation
import logging
from box import Box
from container import Container
from verticalAlgorithm import verticalAlgorithm

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%I:%M:%S', level=logging.DEBUG)

# Decoding data from json[START]
filepath = r"0\30_cl.json"

with open('..\Data\_vg_85_bgg5jsons\\' + filepath, encoding="utf8") as file:
    base = file.read()

jsonString = '{"a":54, "b": 28}'

aDict = json.loads(base)

container = Container(aDict['cargo_space']['id'], aDict['cargo_space']['size'][0], aDict['cargo_space']['size'][1],
                      aDict['cargo_space']['size'][2], aDict['cargo_space']['carrying_capacity'], 0)
logging.info(
    f'Container: id {container.id}, w:{container.width}, h:{container.height}, l{container.length}, cc:{container.maxWeight}')

boxes = []

for item in aDict["cargo_groups"]:
    if item['mass'] <= container.maxWeight:
        boxes.append(Box(item['id'], item['group_id'], item['size'][0], item['size'][1], item['size'][2], item['count'],
                         item['mass']))
aDict.clear()
# Decoding data from json[END]


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
container = verticalAlgorithm(0, boxes)[1]


# json encoding[START]
aDict = {'cargoSpace': {'loading_size': container.getSize(), 'position': [0, 0, 0], 'type': 'pallet'}}

# Array contains items of values for keys('cargo_space', 'cargos', 'unpacked')
array = []

for item in container.putCargos:
    boxDict = {'calculated_size': item.getCalculatedSize(), 'cargo_id': item.groupId,
                    'id': item.id, 'mass': item.mass, 'position': item.getPosition(),
                    'size': item.getSize(), 'sort': 0, 'stacking': True, 'turnover': True, 'type': 'box'}
    logging.info(boxDict)
    array.append(boxDict)

aDict = {'cargos': array}

with open('..\Data\\resjson\\' + filepath, 'w', encoding='utf-8') as f:
    json.dump(aDict, f)
    logging.info('Succesfuly encoded data to ' + filepath)
# json encoding[END]

