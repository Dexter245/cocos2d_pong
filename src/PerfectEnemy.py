from Ball import Ball
from Utils import CollidableColorLayer, Direction


class PerfectEnemy(CollidableColorLayer):
    WIDTH = 50
    HEIGHT = 200
    MOVE_SPEED = 200
    COLOR = (255, 255, 255)
    delta = 0.0

    def __init__(self, ball: Ball, position: (int, int)):
        super(PerfectEnemy, self).__init__(position, PerfectEnemy.WIDTH, PerfectEnemy.HEIGHT, PerfectEnemy.COLOR)
        self.ball = ball

    # def move_bat(self, dir: Direction):
    #     self.moveBy((0, dir.value * self.MOVE_SPEED * self.delta))

    def update(self, delta):
        self.delta = delta

        # self.moveBy((0, dir.value * self.MOVE_SPEED * self.delta))
        y = self.ball.y + self.ball.height / 2 - PerfectEnemy.HEIGHT / 2
        if y < 10:
            y = 10
        elif y > 720 - PerfectEnemy.HEIGHT:
            y = 720 - PerfectEnemy.HEIGHT
        self.moveTo((self.x, y))
