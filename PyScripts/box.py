import logging


class Box:
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%I:%M:%S', level=logging.DEBUG)

    def __init__(self, groupId: int, width: int, height: int, length: int, boxCount: int, mass: float):
        self.groupId = groupId
        self.width = width
        self.height = height
        self.length = length
        self.boxCount = boxCount
        self.mass = mass
        # Position is the center of parallelepiped
        self.__position = 0
        logging.info(f'New box: groupId:{groupId} w:{width} h:{height} l:{length} bCount:{boxCount} mass:{mass}')

    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position
