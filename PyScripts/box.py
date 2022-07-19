import logging



class Box:
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%I:%M:%S', level=logging.DEBUG)

    def __init__(self, id: int, groupId: int, width, height, length, boxCount: int, mass: float):
        self.id = id
        self.groupId = groupId
        self.width = width
        self.height = height
        self.length = length
        self.boxCount = boxCount
        self.mass = mass
        # Position is the center of parallelepiped
        self.__position = {}
        self.__constWidth = width
        self.__constLength = length
        self.__constHeight = height
        logging.info(f'New box: groupId:{groupId} w:{width} h:{height} l:{length} bCount:{boxCount} mass:{mass}')

    def setPosition(self, position):
        self.__position = position  # position = {"width" : .., "height" : .., "length" : ..}

    def getPosition(self):
        return self.__position.copy()

    def getPositionInMeters(self):
        position = self.__position.copy()

        return {'x': position['length']/2000, 'y': position['height']/1000, 'z': position['width']/1000}

    def getSize(self):
        return {'height': self.__constHeight/1000, 'length': self.__constLength/1000,  'width': self.__constWidth/1000}

    def getCalculatedSize(self):
        return {'height': self.height/1000, 'length': self.length/1000, 'width': self.width/1000}

    # rotate box clockwise by 90 degrees along the selected AXIS
    def rotate(self, axis: str):

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

    def getBoxData(self):
        return f' size: w-{self.width} l-{self.length} h-{self.height}'

    def copy(self):
        return Box(self.id, self.groupId, self.width, self.height, self.length, self.boxCount, self.mass)