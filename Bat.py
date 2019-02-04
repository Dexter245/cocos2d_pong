from enum import Enum

import cocos
from cocos.collision_model import AARectShape

from Utils import CollidableColorLayer


class Bat(CollidableColorLayer):
    MOVE_SPEED = 500
    WIDTH = 50
    HEIGHT = 200
    COLOR = (255, 255, 255)
    delta = 0.0

    class Direction(Enum):
        UP = 1
        DOWN = -1
        NONE = 0

    def __init__(self, position: (int, int)):
        super(Bat, self).__init__(position, Bat.WIDTH, Bat.HEIGHT, Bat.COLOR)
        self.dir = self.Direction.NONE
        print("cshape: " + str(self.cshape))

    def move_bat(self, dir: Direction):
        self.moveBy((0, dir.value * self.MOVE_SPEED * self.delta))

    def update(self, delta):
        self.delta = delta
        pass
