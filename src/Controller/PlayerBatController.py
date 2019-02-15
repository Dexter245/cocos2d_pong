from pyglet.window import key
from cocos.layer import Layer

from Controller.BatController import BatController


class PlayerBatController(BatController, Layer):

    def __init__(self):
        super(PlayerBatController, self).__init__()

        self.keys_pressed = []
        self.is_event_handler = True

    def update(self, delta: float):
        pass

    def on_key_press(self, k, modifiers):
        # print("on_key_press")
        self.keys_pressed.append(key)
        if k == key.W:
            self.action_up = True
        elif k == key.S:
            self.action_down = True


    def on_key_release(self, k, modifiers):
        # print("on_key_release")
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)
        if k == key.W:
            self.action_up = False
        elif k == key.S:
            self.action_down = False
