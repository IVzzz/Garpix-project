from box import Box
from container import Container


# get sum of all boxes volume from list
def CountAllVolume(boxes: list):
    totalVolume = 0
    for box in boxes:
        totalVolume += (box.width * box.height * box.length) * box.boxCount
    return totalVolume


# get dictionary of box amount in every group
def GetBoxAmountList(boxes: list):
    amountList = {}
    for box in boxes:
        amountList[str(box.groupId)] = box.boxCount
    return amountList


# get mass of all boxes
def GetBoxesMass(boxes: list):
    totalMass = 0
    for box in boxes:
        totalMass += boxes.mass
    return totalMass


def verticalAlgorithm(commonParam: int, boxes: list):
    maxWeight = int(Container.maxWeight * (commonParam / Container.width) / (0.75))
    trialContainer = Container(0, commonParam, Container.height, Container.length, maxWeight)
    volume = trialContainer.width * trialContainer.height * trialContainer.length
    volumeBoxes = 0  # volume of boxes which were placed in trial Container
    ContainerVolume = commonParam * trialContainer.height * trialContainer.length
    boxLineLength = 0
    towersList = []  # list of positions for new box placing

    totalVolume = CountAllVolume(boxes)
    amountList = GetBoxAmountList(boxes)
    totalMass = GetBoxesMass(boxes)

    position = {"width": 0, "height": 0, "length": 0}
    towersList.append([position, 0])
    for box in boxes:
        boxVolume = box.width * box.height * box.length
        if totalMass > maxWeight and box.mass / boxVolume > maxWeight / ContainerVolume:
            continue
        wasAdded = True
        while amountList[str(box.groupId)] > 0 and wasAdded:
            wasAdded = False
            countPositions = len(towersList)
            for i in range(countPositions):
                nextPos = towersList[i][0]
                nextPos["height"] = box.height / 2 + towersList[i][0]["height"]
                nextPos["length"] = box.length / 2 + towersList[i][0]["length"]
                nextPos["width"] = box.width / 2
                if trialContainer.addBox(box, nextPos):
                    amountList[str(box.groupId)] -= 1
                    volumeBoxes += boxVolume
                    if towersList[i][0]["height"] != 0 and box.length < towersList[i][1]:
                        newPos = towersList[i]
                        newPos[0]["length"] += box.length
                        towersList.insert(i + 1, newPos)
                    towersList[i][0]["height"] += box.height
                    towersList[i][1] = box.length
                    boxLineLength += box.length
                    wasAdded = True
                    break
                elif i + 1 == len(towersList) and boxLineLength + box.length < trialContainer.length:
                    nextPos = towersList[i][0]
                    position["height"] = 0
                    position["length"] = boxLineLength
                    position["width"] = 0
                    nextPos["width"] = box.width / 2
                    nextPos["height"] = box.height / 2
                    nextPos["length"] = box.length / 2 + boxLineLength
                    if trialContainer.addBox(box, nextPos):
                        wasAdded = True
                        amountList[str(box.groupId)] -= 1
                        volumeBoxes += box.width * box.height * box.length
                        towersList.append([position, box.length + towersList[i][1]])

    return [volumeBoxes / volume, trialContainer]
