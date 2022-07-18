from box import Box


def fragmentationBoxes(boxes):
    classes = {}
    for i in range(0, len(boxes)):
        if boxes[i].boxCount == 0:
            continue
        for t in range(3):
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
                    for k in range(len(buffer_)):
                        if (buffer_[k].id == idBox):
                            idFlag = True
            if (idFlag == False):
                newbox = boxes[i].copy()
                if t == 1:
                    newbox.rotate("x")
                elif t == 2:
                    newbox.rotate("z")

                if not keyClass in classes.keys():
                    classes[keyClass] = [newbox]
                else:
                    buffer = classes[keyClass]
                    buffer.append(newbox)
                    classes[keyClass] = buffer.copy()
    return classes