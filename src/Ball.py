from enum import Enum

from Utils import CollidableColorLayer


class Ball(CollidableColorLayer):
    WIDTH = 50
    HEIGHT = 50
    MOVE_SPEED = 250
    COLOR = (255, 255, 255)
    delta = 0.0

    class Direction(Enum):
        NONE = (0, 0)
        LEFT_UP = (-1, 1)
        LEFT_DOWN = (-1, -1)
        RIGHT_UP = (1, 1)
        RIGHT_DOWN = (1, -1)

    def __init__(self, position: (int, int)):
        super(Ball, self).__init__(position, Ball.WIDTH, Ball.HEIGHT, Ball.COLOR)
        self.dir = Ball.Direction.NONE
        self.dir = Ball.Direction.LEFT_UP

    def update(self, delta):
        self.delta = delta
        self.__move_ball()

    def flip_x_dir(self):
        if self.dir == Ball.Direction.LEFT_UP:
            self.dir = Ball.Direction.RIGHT_UP
        elif self.dir == Ball.Direction.LEFT_DOWN:
            self.dir = Ball.Direction.RIGHT_DOWN
        elif self.dir == Ball.Direction.RIGHT_UP:
            self.dir = Ball.Direction.LEFT_UP
        elif self.dir == Ball.Direction.RIGHT_DOWN:
            self.dir = Ball.Direction.LEFT_DOWN

    def flip_y_dir(self):
        if self.dir == Ball.Direction.LEFT_UP:
            self.dir = Ball.Direction.LEFT_DOWN
        elif self.dir == Ball.Direction.LEFT_DOWN:
            self.dir = Ball.Direction.LEFT_UP
        elif self.dir == Ball.Direction.RIGHT_UP:
            self.dir = Ball.Direction.RIGHT_DOWN
        elif self.dir == Ball.Direction.RIGHT_DOWN:
            self.dir = Ball.Direction.RIGHT_UP

    def __move_ball(self):
        print("dir: " + str(self.dir) + ", dir.value: " + str(self.dir.value) + ", value0: " +
              str(self.dir.value[0]) + ", value1: " + str(self.dir.value[1]))
        self.moveBy((self.dir.value[0] * Ball.MOVE_SPEED * self.delta,
                     self.dir.value[1] * Ball.MOVE_SPEED * self.delta))
