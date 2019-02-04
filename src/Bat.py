from src.Utils import CollidableColorLayer, Direction


class Bat(CollidableColorLayer):
    MOVE_SPEED = 500
    WIDTH = 50
    HEIGHT = 200
    COLOR = (255, 255, 255)
    delta = 0.0

    def __init__(self, position: (int, int)):
        super(Bat, self).__init__(position, Bat.WIDTH, Bat.HEIGHT, Bat.COLOR)
        self.dir = Direction.NONE
        print("cshape: " + str(self.cshape))

    def move_bat(self, dir: Direction):
        self.moveBy((0, dir.value * self.MOVE_SPEED * self.delta))

    def update(self, delta):
        self.delta = delta
        pass
