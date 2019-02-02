import cocos
import pyglet

from Bat import Bat
from pyglet.window import key


class Main(cocos.layer.Layer):

    KEY_MOVE_UP = pyglet.window.key.W
    KEY_MOVE_DOWN = pyglet.window.key.S

    def __init__(self):
        super(Main, self).__init__()

        self.is_event_handler = True
        self.keys_pressed = []
        cocos.director.director.set_show_FPS(True)
        self.schedule(self.update)

        self.bat = Bat()
        self.add(self.bat)

    def update(self, delta):
        # print("update delta: " + str(delta))
        self.bat.update(delta)
        print("keys: " + str(self.keys_pressed))
        if key.W in self.keys_pressed:
            self.bat.move(Bat.Direction.UP)
        if key.S in self.keys_pressed:
            self.bat.move(Bat.Direction.DOWN)
        # self.bat.move(Bat.Direction.UP)

    def on_key_press(self, key, modifiers):
        self.keys_pressed.append(key)

    def on_key_release(self, key, modifiers):
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)

    def on_mouse_motion(self, x, y, dx, dy):
        print("on_mouse_motion")
        # self.bat.position = x, y





cocos.director.director.init(width=960, height=1060, resizable=True)
main = Main()
main_scene = cocos.scene.Scene(main)
cocos.director.director.run(main_scene)
