from box import Box
from container import Container

# get sum of all boxes volume from list
def CountAllVolume(boxes : list):
    totalVolume = 0
    for box in boxes:
        totalVolume += (box.width * box.height * box.length) * box.boxCount
    return totalVolume

# get dictionary of box amount in every group
def GetBoxAmountList(boxes : list):
    amountList = {}
    for box in boxes:
        amountList[str(box.groupId)] = box.boxCount
    return amountList

# get mass of all boxes
def GetBoxesMass(boxes : list):
    totalMass = 0
    for box in boxes:
        totalMass += box.mass
    return totalMass

def VerticalAlgorithm(commonParam : int, boxes : list, container, coff):
    maxWeight = int((container.maxWeight - container.currentWeight) * coff)
    trialContainer = Container(0, commonParam, container.height, container.length, maxWeight)
    volume = trialContainer.width * trialContainer.height * trialContainer.length
    volumeBoxes = 0 # volume of boxes which were placed in trial container
    boxLineLength = 0
    towersList = [] # list of positions for new box placing

    totalVolume = CountAllVolume(boxes)
    amountList = GetBoxAmountList(boxes)
    totalMass = GetBoxesMass(boxes)

    position = {"width": 0, "height": 0, "length": 0}
    towersList.append([position, container.length, commonParam])
    for box in boxes:
        boxVolume = box.width * box.height * box.length
        wasAdded = True
        while amountList[str(box.groupId)] > 0 and wasAdded:
            wasAdded = False
            countPositions = len(towersList)
            for i in range(countPositions):
                nextPos = towersList[i][0].copy()
                nextPos["height"] = box.height / 2 + towersList[i][0]["height"]
                nextPos["length"] = box.length / 2 + towersList[i][0]["length"]
                nextPos["width"] = box.width / 2 + towersList[i][0]["width"]
                rotate = "n"
                if trialContainer.addBox(box, nextPos):
                    rotate = "c"
                else:
                    box.rotate("z")
                    if trialContainer.addBox(box, nextPos):
                        rotate = "z"
                    else:
                        box.rotate("y")
                        if trialContainer.addBox(box, nextPos):
                            rotate = "y"
                        else:
                            box.rotate("x")
                            if trialContainer.addBox(box, nextPos):
                                rotate = "x"

                if rotate != "n":
                    amountList[str(box.groupId)] -= 1
                    volumeBoxes += boxVolume
                    pos = i

                    if box.width < towersList[i][2]:
                        newPos = towersList[i].copy()
                        newPos[0]["width"] += box.width
                        newPos[2] = towersList[i][2] - box.width
                        pos += 1
                        towersList.insert(pos, newPos)

                    if towersList[i][0]["height"] != 0 and box.length < towersList[i][1]:
                        newPos = towersList[i].copy()
                        newPos[0]["length"] += box.length
                        newPos[1] = towersList[i][1] - box.length
                        pos += 1
                        towersList.insert(pos, newPos)

                    if towersList[i][0]["height"] != 0 and box.width < towersList[i][2] and box.length < towersList[i][1]:
                        newPos = towersList[i].copy()
                        newPos[0]["length"] += box.length
                        newPos[0]["width"] += box.width
                        newPos[2] = towersList[i][2] - box.width
                        newPos[1] = towersList[i][1] - box.length
                        pos += 1
                        towersList.insert(pos, newPos)

                    towersList[i][0]["height"] += box.height
                    towersList[i][1] = box.length
                    towersList[i][2] = box.width
                    boxLineLength += box.length
                    wasAdded = True
                    if rotate != "c":
                        box.rotate(rotate)
                    break
                elif i + 1 == len(towersList) and boxLineLength + box.length < trialContainer.length:
                    nextPos = towersList[i][0].copy()
                    position["height"] = 0
                    position["length"] = boxLineLength
                    position["width"] = 0
                    nextPos["width"] = box.width / 2
                    nextPos["height"] = box.height / 2
                    nextPos["length"] = box.length / 2 + boxLineLength
                    if trialContainer.addBox(box, nextPos):
                        wasAdded = True
                        amountList[str(box.groupId)] -= 1
                        volumeBoxes += boxVolume
                        towersList.append([position, box.length + towersList[i][1], box.width])
    return [volumeBoxes/volume, trialContainer]


def ChooseOptimalLayer(boxClasses, container):
    layers = {}
    maxEff = 0
    maxLayer = 0
    for commonParam in boxClasses.keys():
        res = VerticalAlgorithm(commonParam, boxClasses[commonParam], container, 0.5)
        if maxEff <= res[0] and res[1].currentWeight <= container.maxWeight - container.currentWeight and res[1].width <= container.width - container.currentWidth:
            if maxEff == res[0] and maxLayer > commonParam:
                maxLayer = commonParam
            else:
                maxEff = res[0]
                maxLayer = commonParam
        layers[commonParam] = res[1]
    if maxLayer != 0:
        for box in layers[maxLayer].putCargos:
            pos = box.getPosition().copy()
            a = container.addBox(box, pos)
            for item in boxClasses[maxLayer]:
                if item.groupId == box.groupId:
                    box.boxCount -= 1
        container.currentWidth += layers[maxLayer].width
        return True
    else:
        return False

