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
        self.__position = {'x': 0, 'y': 0, 'z': 0}
        logging.info(f'New box: groupId:{groupId} w:{width} h:{height} l:{length} bCount:{boxCount} mass:{mass}')

    def setPosition(self, x: int, y: int, z: int):
        self.__position.update({'x': x, 'y': y, 'z': z})

    def getPosition(self):
        return self.__position.copy()

    # rotate box clockwise by DEGREES along the selected AXIS
    def rotate(self, degrees: int, axis: str):
        buffer = 0
        if degrees == 90:
            if axis == "x":
                buffer = self.width
                self.width = self.height
                self.height = buffer
            elif axis == "y":
                buffer = self.length
                self.length = self.height
                self.height = buffer
            elif axis == "z":
                buffer = self.length
                self.length = self.width
                self.width = buffer
