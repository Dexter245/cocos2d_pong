import cocos
import pyglet
from cocos.collision_model import CollisionManager, CollisionManagerGrid, AARectShape, CollisionManagerBruteForce
from cocos.layer import ColorLayer
from cocos.particle import Color

from Bat import Bat
from pyglet.window import key

from Utils import CollidableColorLayer, Direction


class Main(cocos.layer.Layer):
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    KEY_MOVE_UP = pyglet.window.key.W
    KEY_MOVE_DOWN = pyglet.window.key.S

    def __init__(self):
        super(Main, self).__init__()
        print(str(Main.SCREEN_HEIGHT))

        self.is_event_handler = True
        self.keys_pressed = []
        cocos.director.director.set_show_FPS(True)
        self.schedule(self.update)
        self.collisionManager = CollisionManagerBruteForce()

        self.bat = Bat((100, Main.SCREEN_HEIGHT / 2))
        self.add(self.bat)
        self.collisionManager.add(self.bat)

        self.createWalls()

    def update(self, delta):
        print()
        self.bat.update(delta)

        bat_collisions = self.collisionManager.objs_near(self.bat, 0.1)
        bat_collides_top = False
        bat_collides_bottom = False
        for collision in bat_collisions:
            if collision == self.wall_top:
                bat_collides_top = True
            if collision == self.wall_bottom:
                bat_collides_bottom = True
        if key.W in self.keys_pressed:
            if not bat_collides_top:
                self.bat.move_bat(Direction.UP)
        if key.S in self.keys_pressed:
            if not bat_collides_bottom:
                self.bat.move_bat(Direction.DOWN)

    def on_key_press(self, key, modifiers):
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


cocos.director.director.init(width=Main.SCREEN_WIDTH, height=Main.SCREEN_HEIGHT, resizable=True)
main = Main()
main_scene = cocos.scene.Scene(main)
cocos.director.director.run(main_scene)
