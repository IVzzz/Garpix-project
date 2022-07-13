class Box:
    def __init__(self, groupId: int, width: int, height: int, length: int, boxCount: int, mass: float, position: int):
        self.groupId = groupId
        self.width = width
        self.height = height
        self.length = length
        self.boxCount = boxCount
        self.mass = mass
        self.__position = 0

    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position
