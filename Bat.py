from enum import Enum

import cocos


class Bat(cocos.layer.ColorLayer):

    MOVE_SPEED = 500
    delta = 0.0

    class Direction(Enum):
        UP = 1
        DOWN = -1
        NONE = 0

    def __init__(self):
        super(Bat, self).__init__(255, 255, 255, 255, width=50, height=200)
        self.position = 50, 400
        self.dir = self.Direction.NONE

    def move(self, dir: Direction):
        self.y += dir.value * self.MOVE_SPEED * self.delta

    def update(self, delta):
        self.delta = delta
        pass
