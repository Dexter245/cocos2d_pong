from enum import Enum

from cocos.collision_model import AARectShape
from cocos.layer import ColorLayer

class Direction(Enum):
    UP = 1
    DOWN = -1
    LEFT = -1
    RIGHT = 1
    NONE = 0

class CollidableColorLayer(ColorLayer):

    def __init__(self, position: (int, int), width: int, height: int,
                 color: (int, int, int) = (255, 255, 255)):
        super(CollidableColorLayer, self).__init__(255, 255, 255, 255, width=width, height=height)
        self.position = position
        self.color = color
        self.__refreshCShape()

    def moveBy(self, amount: (int, int)):
        self.x += amount[0]
        self.y += amount[1]
        print("amount: " + str(amount))
        self.__refreshCShape()

    def moveTo(self, position: (int, int)):
        self.position = position
        self.__refreshCShape()

    def __refreshCShape(self):
        self.cshape = AARectShape((self.x + self.width / 2, self.y + self.height / 2),
                                  self.width / 2, self.height / 2)
