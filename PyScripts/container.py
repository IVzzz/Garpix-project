from PyScripts.box import Box


class Container:
    def __init__(self, id: int, width: int, height: int, length: int, maxWeight: int, currentWeight):
        self.id = id
        self.width = width
        self.height = height
        self.length = length
        self.maxWeight = maxWeight
        self.currentWeight = currentWeight
        self.putCargos = []

    def addBox(self, box: Box, position):
        if self.maxWeight < box.mass:
            return False
        if position["width"] + box.width / 2 <= self.width - position["width"] and position[
            "width"] - box.width / 2 >= 0:
            if position["height"] + box.height / 2 <= self.height - position["height"] and position[
                "height"] - box.height / 2 >= 0:
                if position["length"] + box.length / 2 <= self.length - position["length"] and position[
                    "length"] - box.length / 2 >= 0:
                    if not self.boxInsideList:
                        self.maxWeight -= box.mass
                        box.setPosition(position)
                        self.boxInsideList.append(box)
                    else:
                        for checkedBox in self.boxInsideList:
                            checkedPosition = checkedBox.getPosition()
                            if abs(checkedPosition["width"] - position.width) >= checkedBox.width / 2 + box.width / 2:
                                if abs(checkedPosition[
                                           "length"] - position.length) >= checkedBox.length / 2 + box.length / 2:
                                    if abs(checkedPosition[
                                               "height"] - position.height) >= checkedBox.height / 2 + box.height / 2:
                                        self.maxWeight -= box.mass
                                        box.setPosition(position)
                                        self.boxInsideList.append(box)
                                        break