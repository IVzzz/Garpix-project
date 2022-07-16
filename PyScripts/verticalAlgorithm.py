originalContainer = Container(id, width, height, length, maxWeight)


def VerticalAlgorithm(commonParam : int, boxes : list):
    trialContainer = originalContainer(0, commonParam, originalContainer.height, originalContainer.length, originalContainer.maxWeight)
    volume = trialContainer.width * trialContainer.height * trialContainer.length
    volumeBoxes = 0
    position = {"width" : 0, "height" : 0, "length" : 0}
    towersList = []
    towersList.append([position, 0])

    for box in boxes:
        if not towersList:
            position["width"] = box.width / 2
            position["height"] = box.height / 2
            position["length"] = box.length / 2
            if trialContainer.addBox(box, position):
                volumeBoxes += (box.width * box.height * box.length)
                towersList[0][1] = box.length
            continue
        for i in range(len(towersList)):
            nextPos = towersList[i][0]
            nextPos["height"] = box.height / 2 + towersList[i][0]["height"]
            nextPos["length"] = box.length / 2 + towersList[i][0]["length"]
            nextPos["width"] = box.width / 2
            if trialContainer.addBox(box, nextPos):
                volumeBoxes += (box.width * box.height * box.length)
                towersList[i][0]["height"] += box.height
                isAdd = True
                break
            elif i + 1 == len(towersList):
                nextPos = towersList[i][0]
                position["height"] = 0
                position["length"] = towersList[i][1]
                position["width"] = 0
                nextPos["width"] = box.width / 2
                nextPos["height"] = box.height / 2
                nextPos["length"] = box.length / 2 + towersList[i][1]
                if box.length + towersList[i][1] <= trialContainer.length:
                    if trialContainer.addBox(box, nextPos):
                        volumeBoxes += (box.width * box.height * box.length)
                        towersList.append([position, box.length + towersList[i][1]])

    return [volumeBoxes/volume, trialContainer]



