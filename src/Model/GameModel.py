from cocos.collision_model import CollisionManagerBruteForce

from Ball import Ball
from Bat import Bat
from PerfectEnemy import PerfectEnemy
from Utils import Gamestate, CollidableColorLayer


class GameModel():

    def __init__(self, fastmode=False, net=None):
        from Main import Main

        self.fastmode = fastmode
        self.net = net
        self.bat = Bat((0, Main.SCREEN_HEIGHT / 2))
        self.collision_manager = CollisionManagerBruteForce()
        self.ball = Ball((1280 / 2, 720 / 2))
        self.enemy = PerfectEnemy(self.ball, (Main.SCREEN_WIDTH - 0 - PerfectEnemy.WIDTH, Main.SCREEN_HEIGHT / 2))
        self.gamestate = Gamestate.RUNNING

        wall_width = 10
        self.wall_left = CollidableColorLayer((40 - wall_width, 0), wall_width, Main.SCREEN_HEIGHT, color=(255, 0, 0))
        self.wall_right = CollidableColorLayer((Main.SCREEN_WIDTH - 50, 0), wall_width,
                                               Main.SCREEN_HEIGHT,
                                               color=(255, 0, 0))
        self.wall_top = CollidableColorLayer((0, Main.SCREEN_HEIGHT - wall_width), Main.SCREEN_WIDTH, wall_width,
                                             color=(255, 0, 0))
        self.wall_bottom = CollidableColorLayer((0, 0), Main.SCREEN_WIDTH, wall_width, color=(255, 0, 0))

        self.score = 0.0
