def fragmentationBoxes(boxes):
    classes = {}
    for i in range(0, len(boxes)):
        if i != 0:
            for width in classes.keys():
                classes[width].append(boxes[i])
        classes[boxes[i].width] = [boxes[i]]
    return classes
