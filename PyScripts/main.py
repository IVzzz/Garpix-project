import json
from getWClasses import fragmentationBoxes
import logging
from box import Box
from container import Container
from verticalAlgorithm import ChooseOptimalLayer
import argparse


def qsort(array, side : str):
    if len(array) <= 1:
        return array
    else:
        lowArray = []
        highArray = []
        equalArray = []
        pivot = 0

        if side == "w":
            pivot = array[int(len(array) / 2)].width
        elif side == "s":
            pivot = array[int(len(array) / 2)].length * array[int(len(array) / 2)].width
        for item in array:
            if side == "s":
                if item.length * item.width < pivot:
                    lowArray.append(item)
                elif item.length * item.width > pivot:
                    highArray.append(item)
                else:
                    equalArray.append(item)
            elif side == "w":
                if item.width < pivot:
                    lowArray.append(item)
                elif item.width > pivot:
                    highArray.append(item)
                else:
                    equalArray.append(item)
        return qsort(highArray, side) + equalArray + qsort(lowArray, side)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%I:%M:%S', level=logging.DEBUG)

    # Decoding data from json[START]
        parser = argparse.ArgumentParser(
        prog="Автозагрузчик",
        description="Заполняет ограниченное трехмерное пространство трехмерными объектами.",
        epilog="(с) SPQR Team"
    )

    parser.add_argument("-p", "--path", default="No path", help="Сюда нужно вводить имя JSON")

    args = parser.parse_args()

    if args.path == "No path":
        print("Enter the path to the file.")

    filepath = args.path
    base = 0

    try:
        with open('/var/tmp/hackathon/data1/' + filepath, "r", encoding="utf8") as file:
            base = file.read()
    except:
        print("The filepath is not correct.")

    jsonString = '{"a":54, "b": 28}'

    aDict = json.loads(base)

    container = Container(aDict['cargo_space']['id'], aDict['cargo_space']['size']["width"], aDict['cargo_space']['size']["height"],
                          aDict['cargo_space']['size']["length"], aDict['cargo_space']['carrying_capacity'])
    container.currentWeight += aDict['cargo_space']['mass']
    logging.info(
        f'Container: id {container.id}, w:{container.width}, h:{container.height}, l{container.length}, cc:{container.maxWeight}')

    boxes = []
    boxes1 = []
    container.maxWeight *= 1000
    container.currentWeight *= 1000

    for item in aDict["cargo_groups"]:
        if item['mass'] <= container.maxWeight:
            boxes.append(Box(item['group_id'], item['group_id'], item['size']["width"], item['size']["height"], item['size']["length"], item['count'],
                             item['mass']))
    aDict.clear()
    # Decoding data from json[END]

    # from kg to gramms
    containerVolume = container.length * container.width * container.height
    brotherContainer = Container(container.id, container.length, container.height, container.width, container.maxWeight)
    for i in boxes:
        boxes1.append(i.copy())
    # Sorting data by non-grown area (quicksort) [START]
    for box in boxes:
        if box.height > box.width and box.height >= box.length:
            box.rotate("x")
        elif box.length > box.width and box.length >= box.height:
            box.rotate("z")
        if box.height > box.length:
            box.rotate("y")
    boxes = qsort(boxes, "w")
    # Sorting data by non-growth (quicksort)[END]
    boxClassesRes1 = fragmentationBoxes(boxes)
    for width in boxClassesRes1.keys():
        boxClassesRes1[width] = qsort(boxClassesRes1[width], "s")

    canAddBoxes = True
    while canAddBoxes:
        canAddBoxes = ChooseOptimalLayer(boxClassesRes1, container)

    totalVolume1 = 0
    for item in container.putCargos:
        totalVolume1 += item.length * item.height * item.width

    eff1 = totalVolume1/containerVolume



    # Sorting data by non-grown area (quicksort) [START]
    for box in boxes1:
        if box.height > box.width and box.height >= box.length:
            box.rotate("x")
        elif box.length > box.width and box.length >= box.height:
            box.rotate("z")
        if box.height > box.length:
            box.rotate("y")
    boxes1 = qsort(boxes1, "w")
    # Sorting data by non-growth (quicksort)[END]
    boxClassesRes2 = fragmentationBoxes(boxes1)
    for width in boxClassesRes2.keys():
        boxClassesRes1[width] = qsort(boxClassesRes1[width], "s")

    canAddBoxes = True
    while canAddBoxes:
        canAddBoxes = ChooseOptimalLayer(boxClassesRes2, brotherContainer)

    totalVolume2 = 0
    for item in brotherContainer.putCargos:
        totalVolume2 += item.length * item.height * item.width

    eff2 = totalVolume2/containerVolume



    if eff1 >= eff2:
        # json encoding[START]
        aDict = {'cargoSpace': {'loading_size': container.getSize(), 'position': container.getPosition(), 'type': 'pallet'}}

        # Array contains items of values for keys('cargo_space', 'cargos', 'unpacked')
        array = []
        idCounter = 0
        for item in container.putCargos:
            boxDict = {'calculated_size': item.getSize(), 'cargo_id': item.groupId,
                       'id': idCounter, 'mass': item.mass, 'position': item.getPositionInMeters(),
                       'size': item.getCalculatedSize(), 'sort': 1, 'stacking': True, 'turnover': True, 'type': 'box'}
            array.append(boxDict)
            idCounter += 1

        aDict.update({'cargos': array})
    else:
        # json encoding[START]
        aDict = {'cargoSpace': {'loading_size': container.getSize(), 'position': container.getPosition(), 'type': 'pallet'}}

        # Array contains items of values for keys('cargo_space', 'cargos', 'unpacked')
        array = []
        idCounter = 0
        for item in brotherContainer.putCargos:
            boxDict = {'calculated_size': item.getSizeReverse(), 'cargo_id': item.groupId,
                       'id': idCounter, 'mass': item.mass, 'position': item.getPositionInMetersReverse(),
                       'size': item.getCalculatedSizeReverse(), 'sort': 1, 'stacking': True, 'turnover': True, 'type': 'box'}
            array.append(boxDict)
            idCounter += 1

        aDict.update({'cargos': array})


    #aDict.update({'unpacked': ''})
    filepath = "res.json"

    with open('/home/group7/output/' + filepath, 'w', encoding='utf-8') as f:
        json.dump(aDict, f)
        logging.info('Succesfuly encoded data to ' + filepath)
    # json encoding[END]
