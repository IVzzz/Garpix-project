from box import Box

def fragmentationBoxes(boxes):

    classes = {}

    newBoxes = []

    for i in range (0, len(boxes)):
        for t in range (3):
            if (t == 0):
                keyClass = boxes[i].width
            elif (t == 1):
                keyClass = boxes[i].height
            else:
                keyClass = boxes[i].length

            idBox = boxes[i].id
            idFlag = False
            for s in classes.keys():
                if (keyClass == s):
                    buffer_ = classes[s]
                    for k in range (len(buffer_)):
                        if (buffer_[k][2] == idBox):
                            idFlag = True
            if (t == 0 and idFlag == False):
                buffer = (boxes[i].height, boxes[i].length, boxes[i].id, boxes[i].boxCount)
                classes.setdefault(keyClass, []).append(buffer)
                newBoxes.append(Box(boxes[i].id, boxes[i].groupId, boxes[i].width, boxes[i].height, boxes[i].length, boxes[i].boxCount, boxes[i].mass))
            elif (t == 1 and idFlag == False):
                buffer = (boxes[i].width, boxes[i].length, boxes[i].id, boxes[i].boxCount)
                classes.setdefault(keyClass, []).append(buffer)
                newBoxes.append(Box(boxes[i].id, boxes[i].groupId, boxes[i].height, boxes[i].width, boxes[i].length, boxes[i].boxCount, boxes[i].mass))
            elif (idFlag == False):
                buffer = (boxes[i].width, boxes[i].height, boxes[i].id, boxes[i].boxCount)
                classes.setdefault(keyClass, []).append(buffer)
                newBoxes.append(Box(boxes[i].id, boxes[i].groupId, boxes[i].length, boxes[i].width, boxes[i].height, boxes[i].boxCount, boxes[i].mass))
            
            """
            for s in classes.keys():
                if (keyClass == s):
                    buffer_ = classes[s]
                    for k in range (len(buffer_)):
                        if (buffer_[k][2] == idBox):
                            idFlag = True
            if (t == 0 and idFlag == False):
                buffer = (boxes[i][2][t + 1], boxes[i][2][t + 2], boxes[i][0], boxes[i][3])
                classes.setdefault(keyClass, []).append(buffer)
            elif (t == 1 and idFlag == False):
                buffer = (boxes[i][2][t - 1], boxes[i][2][t + 1], boxes[i][0], boxes[i][3])
                classes.setdefault(keyClass, []).append(buffer)
            elif (idFlag == False):
                buffer = (boxes[i][2][t - 2], boxes[i][2][t - 1], boxes[i][0], boxes[i][3])
                classes.setdefault(keyClass, []).append(buffer)

"""
    sortedClasses = dict(sorted(classes.items()))

    print(sortedClasses)
    return newBoxes