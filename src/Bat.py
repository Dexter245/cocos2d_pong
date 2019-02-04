from enum import Enum

from Utils import CollidableColorLayer


class Bat(CollidableColorLayer):
    WIDTH = 50
    HEIGHT = 200
    MOVE_SPEED = 200
    COLOR = (255, 255, 255)
    delta = 0.0

    class Direction(Enum):
        UP = 1
        DOWN = -1
        LEFT = -1
        RIGHT = 1
        NONE = 0

    def __init__(self, position: (int, int)):
        super(Bat, self).__init__(position, Bat.WIDTH, Bat.HEIGHT, Bat.COLOR)
        # self.dir = Bat.Direction.NONE
        # print("cshape: " + str(self.cshape))

    def update(self, delta):
        self.delta = delta

    def move_bat(self, dir: Direction):
        self.moveBy((0, dir.value * self.MOVE_SPEED * self.delta))

