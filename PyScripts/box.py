import logging
import math
import numpy


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
        self.__position = []
        self.__constWidth = width
        self.__constLength = length
        self.__constHeight = height
        logging.info(f'New box: groupId:{groupId} w:{width} h:{height} l:{length} bCount:{boxCount} mass:{mass}')

    def setPosition(self, x, y, z):
        self.__position = {'x': x, 'y': y, 'z': z}

    def getPosition(self):
        return self.__position.copy()

    def getSize(self):
        return {'height': self.__constHeight, 'length': self.__constLength,  'width': self.__constWidth}

    def getCalculatedSize(self):
        return {'height': self.height, 'length': self.length, 'width': self.width}

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

    # Function returns numpy array of 4 vertexes of the box
    def getVertices(self):
        diagonal = math.sqrt(self.width * self.width + self.length * self.length + self.height * self.height)

        vertices = numpy.array([])
        vertex = numpy.array([0, 0, 0])

        halfWidth = self.width/2
        halfLength = self.length/2
        halfHeight = self.height/2

        # Counting 8 vertices of the box by adding up position +- 1/2 * width/length/height
        vertex = numpy.array([self.__position[0] + halfLength, self.__position[1] - halfWidth, self.__position[2] - halfHeight])
        vertices = vertex

        vertex = numpy.array([self.__position[0] - halfLength, self.__position[1] - halfWidth, self.__position[2] - halfHeight])
        vertices = numpy.vstack((vertices, vertex))

        vertex = [self.__position[0] - halfLength, self.__position[1] + halfWidth, self.__position[2] - halfHeight]
        vertices = numpy.vstack((vertices, vertex))

        vertex = [self.__position[0] + halfLength, self.__position[1] + halfWidth, self.__position[2] - halfHeight]
        vertices = numpy.vstack((vertices, vertex))

        vertex = [self.__position[0] + halfLength, self.__position[1] - halfWidth, self.__position[2] + halfHeight]
        vertices = numpy.vstack((vertices, vertex))

        vertex = [self.__position[0] - halfLength, self.__position[1] - halfWidth, self.__position[2] + halfHeight]
        vertices = numpy.vstack((vertices, vertex))

        vertex = [self.__position[0] - halfLength, self.__position[1] + halfWidth, self.__position[2] + halfHeight]
        vertices = numpy.vstack((vertices, vertex))

        vertex = [self.__position[0] + halfLength, self.__position[1] + halfWidth, self.__position[2] + halfHeight]
        vertices = numpy.vstack((vertices, vertex))

        return vertices

    def getBoxData(self):
        #return f'id: {self.id} size: w-{self.width} l-{self.length} h-{self.height} mass: {self.mass} count: {self.boxCount}\n'
        return f' size: w-{self.width} l-{self.length} h-{self.height}'
