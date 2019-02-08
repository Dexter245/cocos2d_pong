import cocos
import pyglet
import time
from cocos.collision_model import CollisionManagerBruteForce
from cocos.text import Label

from Ball import Ball
from Bat import Bat
from pyglet.window import key

from PerfectEnemy import PerfectEnemy
from Utils import CollidableColorLayer, Direction, Gamestate


class Main(cocos.layer.Layer):
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    KEY_MOVE_UP = pyglet.window.key.W
    KEY_MOVE_DOWN = pyglet.window.key.S

    def __init__(self, fastmode:bool = False):
        super(Main, self).__init__()
        print(str(Main.SCREEN_HEIGHT))

        self.fastmode = fastmode
        self.is_event_handler = True
        self.keys_pressed = []
        cocos.director.director.set_show_FPS(True)
        self.schedule(self.update)
        self.collisionManager = CollisionManagerBruteForce()

        self.bat = Bat((100, Main.SCREEN_HEIGHT / 2))
        self.add(self.bat)
        self.collisionManager.add(self.bat)
        self.ball = Ball((1280 / 2, 720 / 2))
        self.add(self.ball)
        self.collisionManager.add(self.ball)
        self.enemy = PerfectEnemy(self.ball, (Main.SCREEN_WIDTH - 100 - PerfectEnemy.WIDTH, Main.SCREEN_HEIGHT / 2))
        self.add(self.enemy)
        self.collisionManager.add(self.enemy)

        self.createWalls()

        self.label_time = Label("Time: ", font_name="Arial", font_size=36, align="center")
        self.label_time.position = (Main.SCREEN_WIDTH/2, Main.SCREEN_HEIGHT/2)
        self.add(self.label_time)

        self.gamestate = Gamestate.RUNNING
        self.score = 0.0

    def update(self, delta):
        print()
        if self.fastmode:
            delta = 0.16
        if self.gamestate == Gamestate.RUNNING:
            self.score += delta
            self.label_time.element.text = "%.1fs" % self.score
            self.bat.update(delta)
            self.ball.update(delta)
            self.enemy.update(delta)

        bat_collisions = self.collisionManager.objs_near(self.bat, 0.0001)

        if key.W in self.keys_pressed:
            if not self.wall_top in bat_collisions:
                self.bat.move_bat(Direction.UP)
        if key.S in self.keys_pressed:
            if not self.wall_bottom in bat_collisions:
                self.bat.move_bat(Direction.DOWN)

        ball_collisions = self.collisionManager.objs_near(self.ball, 0.0001)
        print("ball_collisions: " + str(ball_collisions))
        if self.wall_top in ball_collisions or self.wall_bottom in ball_collisions:
            self.ball.flip_y_dir()
        if self.bat in ball_collisions or self.enemy in ball_collisions:
            self.ball.flip_x_dir()
        if self.wall_left in ball_collisions:
            self.on_game_end()
            pass
        if self.wall_right in ball_collisions:
            # todo: earn point
            self.ball.flip_x_dir()
        # time.sleep(2)

    def on_game_end(self):
        print("on_game_end. time: " + str(self.score))
        self.gamestate = Gamestate.ENDED
        cocos.director.director.scene.end(self.score)

    def on_key_press(self, key, modifiers):
        print("on_key_press")
        self.keys_pressed.append(key)

    def on_key_release(self, key, modifiers):
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)

    def on_mouse_motion(self, x, y, dx, dy):
        pass
        # print("on_mouse_motion")
        # self.bat.position = x, y

    def createWalls(self):
        # left
        wall_width = 10
        self.wall_left = CollidableColorLayer((0, 0), wall_width, Main.SCREEN_HEIGHT, color=(255, 0, 0))
        self.add(self.wall_left)
        self.collisionManager.add(self.wall_left)
        # right
        self.wall_right = CollidableColorLayer((Main.SCREEN_WIDTH - wall_width, 0), wall_width, Main.SCREEN_HEIGHT,
                                               color=(255, 0, 0))
        self.add(self.wall_right)
        self.collisionManager.add(self.wall_right)
        # top
        self.wall_top = CollidableColorLayer((0, Main.SCREEN_HEIGHT - wall_width), Main.SCREEN_WIDTH, wall_width,
                                             color=(255, 0, 0))
        self.add(self.wall_top)
        self.collisionManager.add(self.wall_top)
        # bottom
        self.wall_bottom = CollidableColorLayer((0, 0), Main.SCREEN_WIDTH, wall_width, color=(255, 0, 0))
        self.add(self.wall_bottom)
        self.collisionManager.add(self.wall_bottom)


cocos.director.director.init(width=Main.SCREEN_WIDTH, height=Main.SCREEN_HEIGHT, resizable=True, vsync=False)
main = Main(fastmode=False)
# main = Main(fastmode=True)
main_scene = cocos.scene.Scene(main)
cocos.director.director.run(main_scene)
score = cocos.director.director.return_value
print("score: " + str(score))
