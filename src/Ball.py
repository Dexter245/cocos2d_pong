from enum import Enum

from Utils import CollidableColorLayer


class Ball(CollidableColorLayer):
    WIDTH = 50
    HEIGHT = 50
    MOVE_SPEED = 500
    COLOR = (255, 255, 255)
    DELTA = MOVE_SPEED / 50.0

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
            self.moveBy((Ball.DELTA, 0))
        elif self.dir == Ball.Direction.LEFT_DOWN:
            self.dir = Ball.Direction.RIGHT_DOWN
            self.moveBy((Ball.DELTA, 0))
        elif self.dir == Ball.Direction.RIGHT_UP:
            self.dir = Ball.Direction.LEFT_UP
            self.moveBy((-Ball.DELTA, 0))
        elif self.dir == Ball.Direction.RIGHT_DOWN:
            self.dir = Ball.Direction.LEFT_DOWN
            self.moveBy((-Ball.DELTA, 0))

    def flip_y_dir(self):
        if self.dir == Ball.Direction.LEFT_UP:
            self.dir = Ball.Direction.LEFT_DOWN
            self.moveBy((0, -Ball.DELTA))
        elif self.dir == Ball.Direction.LEFT_DOWN:
            self.dir = Ball.Direction.LEFT_UP
            self.moveBy((0, Ball.DELTA))
        elif self.dir == Ball.Direction.RIGHT_UP:
            self.dir = Ball.Direction.RIGHT_DOWN
            self.moveBy((0, -Ball.DELTA))
        elif self.dir == Ball.Direction.RIGHT_DOWN:
            self.dir = Ball.Direction.RIGHT_UP
            self.moveBy((0, Ball.DELTA))

    def __move_ball(self):
        # print("dir: " + str(self.dir) + ", dir.value: " + str(self.dir.value) + ", value0: " +
        #       str(self.dir.value[0]) + ", value1: " + str(self.dir.value[1]))
        self.moveBy((self.dir.value[0] * Ball.MOVE_SPEED * self.delta,
                     self.dir.value[1] * Ball.MOVE_SPEED * self.delta))
