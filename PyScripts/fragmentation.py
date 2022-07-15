def fragmentationBoxes(boxes):

    classes = {}

    for i in range(1, len(boxes)):
        for t in range(3):
            keyClass = boxes[i][2][t]
            idBox = boxes[i][0]
            idFlag = False
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
    sortedClasses = dict(sorted(classes.items()))
    return sortedClasses
